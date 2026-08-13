// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

/**
 * @title ORFSlaVault
 * @author Christian Taylor · Open Source Frontiers Lab (LF Decentralized Trust)
 * @notice Native EVM Smart Contract for Open Replenishment Framework (ORF) Enterprise SLAs
 * @dev Handles commercial maintenance SLA deposits, reciprocal fee routing, and automated maintainer streaming.
 */
contract ORFSlaVault {
    
    // --- Governance & Roles ---
    address public dOSPOAdmin;
    address public treasuryRecipient;
    uint256 public constant MAX_RECIPROCAL_BPS = 500; // Max 5.0% reciprocal fee

    struct SLABundle {
        address client;
        uint256 annualFee;
        uint256 expirationTimestamp;
        uint256 reciprocalBps; // Fee split in basis points (100 = 1.0%)
        bool isActive;
        string repoIdentifier;
    }

    // Mapping of client address => SLA Bundle
    mapping(address => SLABundle) public slaBundles;
    
    // Maintainer Retainer Streams
    mapping(address => uint256) public maintainerStreamRatesPerSecond;
    mapping(address => uint256) public maintainerLastClaimedTimestamp;

    // --- Events ---
    event SLAPurchased(address indexed client, string repoIdentifier, uint256 annualFee, uint256 expirationTimestamp);
    event ReciprocalFeeReceived(address indexed client, uint256 amount);
    event MaintainerStipendClaimed(address indexed maintainer, uint256 amount);
    event dOSPOAdminTransferred(address indexed oldAdmin, address indexed newAdmin);

    modifier onlyDOSPO() {
        require(msg.sender == dOSPOAdmin, "ORF: Caller is not dOSPO admin");
        _;
    }

    constructor(address _dOSPOAdmin, address _treasuryRecipient) {
        require(_dOSPOAdmin != address(0), "ORF: Invalid admin");
        require(_treasuryRecipient != address(0), "ORF: Invalid treasury");
        dOSPOAdmin = _dOSPOAdmin;
        treasuryRecipient = _treasuryRecipient;
    }

    /**
     * @notice Purchase an Enterprise Maintenance SLA bundle for a specific open-source repo
     * @param repoIdentifier GitHub / Ecosystem repo string
     * @param durationSeconds Coverage period in seconds (e.g. 365 days)
     * @param reciprocalBps Agreed reciprocal revenue share in basis points
     */
    function purchaseSLA(
        string calldata repoIdentifier,
        uint256 durationSeconds,
        uint256 reciprocalBps
    ) external payable {
        require(msg.value > 0, "ORF: SLA fee must be > 0");
        require(reciprocalBps <= MAX_RECIPROCAL_BPS, "ORF: Exceeds max reciprocal BPS");

        uint256 expiration = block.timestamp + durationSeconds;
        
        slaBundles[msg.sender] = SLABundle({
            client: msg.sender,
            annualFee: msg.value,
            expirationTimestamp: expiration,
            reciprocalBps: reciprocalBps,
            isActive: true,
            repoIdentifier: repoIdentifier
        });

        // 80% to Treasury, 20% retained for maintainer retainer stream buffer
        uint256 treasuryShare = (msg.value * 80) / 100;
        (bool sent, ) = payable(treasuryRecipient).call{value: treasuryShare}("");
        require(sent, "ORF: Failed to route treasury payment");

        emit SLAPurchased(msg.sender, repoIdentifier, msg.value, expiration);
    }

    /**
     * @notice Deposit reciprocal commercial revenue share under SLA contract terms
     */
    function depositReciprocalFee() external payable {
        SLABundle storage sla = slaBundles[msg.sender];
        require(sla.isActive, "ORF: No active SLA bundle");
        require(msg.value > 0, "ORF: Reciprocal fee must be > 0");

        (bool sent, ) = payable(treasuryRecipient).call{value: msg.value}("");
        require(sent, "ORF: Failed to route reciprocal fee");

        emit ReciprocalFeeReceived(msg.sender, msg.value);
    }

    /**
     * @notice Set maintainer streaming rate (OMF Maintainer Retainer)
     */
    function setMaintainerStream(address maintainer, uint256 ratePerSecond) external onlyDOSPO {
        require(maintainer != address(0), "ORF: Invalid maintainer");
        
        // Claim pending before update
        _claimMaintainerStipend(maintainer);
        
        maintainerStreamRatesPerSecond[maintainer] = ratePerSecond;
        maintainerLastClaimedTimestamp[maintainer] = block.timestamp;
    }

    /**
     * @notice Claim accrued maintainer retainer stipend
     */
    function claimMaintainerStipend() external {
        _claimMaintainerStipend(msg.sender);
    }

    function _claimMaintainerStipend(address maintainer) internal {
        uint256 rate = maintainerStreamRatesPerSecond[maintainer];
        if (rate == 0) return;

        uint256 lastClaim = maintainerLastClaimedTimestamp[maintainer];
        uint256 timeElapsed = block.timestamp - lastClaim;
        if (timeElapsed == 0) return;

        uint256 amountToClaim = timeElapsed * rate;
        maintainerLastClaimedTimestamp[maintainer] = block.timestamp;

        uint256 contractBalance = address(this).balance;
        if (amountToClaim > contractBalance) {
            amountToClaim = contractBalance;
        }

        if (amountToClaim > 0) {
            (bool sent, ) = payable(maintainer).call{value: amountToClaim}("");
            require(sent, "ORF: Failed to send maintainer stipend");
            emit MaintainerStipendClaimed(maintainer, amountToClaim);
        }
    }

    /**
     * @notice Transfer dOSPO Admin role (Operator Replaceability)
     */
    function transferDOSPOAdmin(address newAdmin) external onlyDOSPO {
        require(newAdmin != address(0), "ORF: Invalid new admin");
        emit dOSPOAdminTransferred(dOSPOAdmin, newAdmin);
        dOSPOAdmin = newAdmin;
    }

    receive() external payable {}
}
