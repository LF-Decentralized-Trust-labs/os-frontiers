// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

/**
 * @title ORFSlaVault (Architectural Reference Sketch)
 * @notice Open Replenishment Framework (ORF) Enterprise SLA Vault Sketch.
 * @dev Unaudited Stage 0 research candidate implementation with two-step admin transfer, maintainer fee routing, and direct treasury settlement.
 */
contract ORFSlaVault {

    struct SlaAgreement {
        uint256 agreementId;
        address clientAddress;
        uint256 annualFeeWei;
        uint256 expirationTimestamp;
        bool isActive;
    }

    address public governanceExecutor;
    address public pendingGovernanceAdmin;
    address public treasuryAddress;
    address public maintainerPool;
    uint256 public maintainerReinvestmentBps = 1500; // 15.00% Maintainer Reinvestment Split Default

    mapping(address => SlaAgreement) public clientSlas;

    event SlaDeposited(address indexed client, uint256 totalPaid, uint256 maintainerReinvestmentAmount, uint256 netTreasuryAmount);
    event MaintainerReinvestmentBpsUpdated(uint256 newBps);
    event GovernanceAdminTransferStarted(address indexed currentAdmin, address indexed pendingAdmin);
    event GovernanceAdminTransferred(address indexed oldAdmin, address indexed newAdmin);
    event TreasuryAddressUpdated(address indexed oldTreasury, address indexed newTreasury);

    modifier onlyAdmin() {
        require(msg.sender == governanceExecutor, "ORF: Caller is not governance executor");
        _;
    }

    constructor(address _governanceExecutor, address _treasuryAddress, address _maintainerPool) {
        require(_governanceExecutor != address(0), "ORF: Invalid executor address");
        require(_treasuryAddress != address(0), "ORF: Invalid treasury address");
        require(_maintainerPool != address(0), "ORF: Invalid maintainer pool address");
        governanceExecutor = _governanceExecutor;
        treasuryAddress = _treasuryAddress;
        maintainerPool = _maintainerPool;
    }

    /**
     * @notice Initiates two-step admin transfer.
     */
    function transferGovernanceAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "ORF: Invalid new admin address");
        pendingGovernanceAdmin = _newAdmin;
        emit GovernanceAdminTransferStarted(governanceExecutor, _newAdmin);
    }

    /**
     * @notice Accepts two-step admin transfer.
     */
    function acceptGovernanceAdmin() external {
        require(msg.sender == pendingGovernanceAdmin, "ORF: Caller is not pending admin");
        emit GovernanceAdminTransferred(governanceExecutor, pendingGovernanceAdmin);
        governanceExecutor = pendingGovernanceAdmin;
        pendingGovernanceAdmin = address(0);
    }

    function setTreasuryAddress(address _newTreasury) external onlyAdmin {
        require(_newTreasury != address(0), "ORF: Invalid new treasury address");
        emit TreasuryAddressUpdated(treasuryAddress, _newTreasury);
        treasuryAddress = _newTreasury;
    }

    function setMaintainerReinvestmentBps(uint256 _newBps) external onlyAdmin {
        require(_newBps <= 5000, "ORF: Reinvestment split cannot exceed 50%");
        maintainerReinvestmentBps = _newBps;
        emit MaintainerReinvestmentBpsUpdated(_newBps);
    }

    function depositSlaFee(uint256 agreementId, uint256 expirationTimestamp) external payable {
        require(msg.value > 0, "ORF: Deposit must be greater than zero");
        require(expirationTimestamp > block.timestamp, "ORF: Expiration must be in the future");

        uint256 maintainerAmount = (msg.value * maintainerReinvestmentBps) / 10000;
        uint256 netTreasuryAmount = msg.value - maintainerAmount;

        clientSlas[msg.sender] = SlaAgreement({
            agreementId: agreementId,
            clientAddress: msg.sender,
            annualFeeWei: msg.value,
            expirationTimestamp: expirationTimestamp,
            isActive: true
        });

        // 1. Route maintainer reinvestment fee split to Maintainer Pool
        if (maintainerAmount > 0) {
            (bool successPool, ) = maintainerPool.call{value: maintainerAmount}("");
            require(successPool, "ORF: Maintainer pool transfer failed");
        }

        // 2. Route remaining net SLA fee directly to Ecosystem Treasury
        if (netTreasuryAmount > 0) {
            (bool successTreasury, ) = treasuryAddress.call{value: netTreasuryAmount}("");
            require(successTreasury, "ORF: Treasury transfer failed");
        }

        emit SlaDeposited(msg.sender, msg.value, maintainerAmount, netTreasuryAmount);
    }

    receive() external payable {
        // Forward un-allocated direct deposits straight to treasury
        if (msg.value > 0) {
            (bool successTreasury, ) = treasuryAddress.call{value: msg.value}("");
            require(successTreasury, "ORF: Direct deposit transfer failed");
        }
    }
}
