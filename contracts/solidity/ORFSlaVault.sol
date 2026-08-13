// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;

/**
 * @title ORFSlaVault (Architectural Reference Sketch)
 * @notice Open Replenishment Framework (ORF) Enterprise SLA Vault Sketch.
 * @dev Unaudited research candidate implementation with reciprocal fee routing and treasury transfer.
 */
contract ORFSlaVault {

    struct SlaAgreement {
        uint256 agreementId;
        address clientAddress;
        uint256 annualFeeWei;
        uint256 expirationTimestamp;
        bool isActive;
    }

    address public dospoAdmin;
    address public treasuryAddress;
    address public maintainerPool;
    uint256 public reciprocalBps = 1500; // 15.00% Reciprocal Fee Split Default

    mapping(address => SlaAgreement) public clientSlas;

    event SlaDeposited(address indexed client, uint256 totalPaid, uint256 reciprocalAmount, uint256 netTreasuryAmount);
    event ReciprocalBpsUpdated(uint256 newBps);
    event DOSPOAdminTransferred(address indexed oldAdmin, address indexed newAdmin);
    event TreasuryAddressUpdated(address indexed oldTreasury, address indexed newTreasury);

    modifier onlyAdmin() {
        require(msg.sender == dospoAdmin, "ORF: Caller is not dOSPO admin");
        _;
    }

    constructor(address _dospoAdmin, address _treasuryAddress, address _maintainerPool) {
        require(_dospoAdmin != address(0), "ORF: Invalid admin address");
        require(_treasuryAddress != address(0), "ORF: Invalid treasury address");
        require(_maintainerPool != address(0), "ORF: Invalid maintainer pool address");
        dospoAdmin = _dospoAdmin;
        treasuryAddress = _treasuryAddress;
        maintainerPool = _maintainerPool;
    }

    function transferDOSPOAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "ORF: Invalid new admin address");
        emit DOSPOAdminTransferred(dospoAdmin, _newAdmin);
        dospoAdmin = _newAdmin;
    }

    function setTreasuryAddress(address _newTreasury) external onlyAdmin {
        require(_newTreasury != address(0), "ORF: Invalid new treasury address");
        emit TreasuryAddressUpdated(treasuryAddress, _newTreasury);
        treasuryAddress = _newTreasury;
    }

    function setReciprocalBps(uint256 _newBps) external onlyAdmin {
        require(_newBps <= 5000, "ORF: Reciprocal fee cannot exceed 50%");
        reciprocalBps = _newBps;
        emit ReciprocalBpsUpdated(_newBps);
    }

    function depositSlaFee(uint256 agreementId, uint256 expirationTimestamp) external payable {
        require(msg.value > 0, "ORF: Deposit must be greater than zero");
        require(expirationTimestamp > block.timestamp, "ORF: Expiration must be in the future");

        uint256 reciprocalAmount = (msg.value * reciprocalBps) / 10000;
        uint256 netTreasuryAmount = msg.value - reciprocalAmount;

        clientSlas[msg.sender] = SlaAgreement({
            agreementId: agreementId,
            clientAddress: msg.sender,
            annualFeeWei: msg.value,
            expirationTimestamp: expirationTimestamp,
            isActive: true
        });

        // 1. Route reciprocal fee split to Maintainer Pool
        if (reciprocalAmount > 0) {
            (bool successPool, ) = maintainerPool.call{value: reciprocalAmount}("");
            require(successPool, "ORF: Maintainer pool transfer failed");
        }

        // 2. Route remaining net SLA fee directly to Ecosystem Treasury
        if (netTreasuryAmount > 0) {
            (bool successTreasury, ) = treasuryAddress.call{value: netTreasuryAmount}("");
            require(successTreasury, "ORF: Treasury transfer failed");
        }

        emit SlaDeposited(msg.sender, msg.value, reciprocalAmount, netTreasuryAmount);
    }

    receive() external payable {
        // Forward un-allocated direct deposits straight to treasury
        if (msg.value > 0) {
            (bool successTreasury, ) = treasuryAddress.call{value: msg.value}("");
            require(successTreasury, "ORF: Direct deposit transfer failed");
        }
    }
}
