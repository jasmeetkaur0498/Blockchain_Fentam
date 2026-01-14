// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract FentanylSupplyChain {
    address public admin;
    uint public drugCount;
    uint public requestCount;

    struct Drug {
        uint id;
        string name;
        string manufacturer;
        uint timestamp;
        address currentOwner;
    }

    struct TxRequest {
        uint id;
        address requestedBy;
        string actionType; // "createDrug" or "transfer"
        string payload;    // "DrugName" or "1,0xNewOwner"
        bool approved;
    }

    mapping(uint => Drug) public drugs;
    mapping(uint => TxRequest) public txRequests;

    // Events
    event RequestSubmitted(uint id, string actionType, string payload, address requestedBy);
    event RequestApproved(uint id);
    event DrugCreated(uint id, string name, address owner);
    event DrugTransferred(uint id, address from, address to);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin allowed");
        _;
    }

    function submitRequest(string memory actionType, string memory payload) public {
        requestCount++;
        txRequests[requestCount] = TxRequest(
            requestCount,
            msg.sender,
            actionType,
            payload,
            false
        );
        emit RequestSubmitted(requestCount, actionType, payload, msg.sender);
    }

    function approveRequest(uint requestId) public onlyAdmin {
        TxRequest storage request = txRequests[requestId];
        require(!request.approved, "Already approved");
        request.approved = true;

        emit RequestApproved(requestId);

        if (keccak256(bytes(request.actionType)) == keccak256("createDrug")) {
            _createDrugFromPayload(request.payload, request.requestedBy);
        } else if (keccak256(bytes(request.actionType)) == keccak256("transfer")) {
            _transferDrugFromPayload(request.payload, request.requestedBy);
        } else {
            revert("Invalid actionType");
        }
    }

    function _createDrugFromPayload(string memory payload, address creator) internal {
        require(bytes(payload).length > 0, "Drug name is empty");
        drugCount++;
        drugs[drugCount] = Drug(
            drugCount,
            payload,
            "VerifiedManufacturer",
            block.timestamp,
            creator
        );
        emit DrugCreated(drugCount, payload, creator);
    }

    function _transferDrugFromPayload(string memory payload, address sender) internal {
        (uint drugId, address newOwner) = _parseTransferPayload(payload);
        Drug storage drug = drugs[drugId];
        require(drug.id != 0, "Drug does not exist");
        require(drug.currentOwner == sender, "Not authorized to transfer");

        drug.currentOwner = newOwner;
        emit DrugTransferred(drugId, sender, newOwner);
    }

    function _parseTransferPayload(string memory payload) internal pure returns (uint, address) {
        bytes memory b = bytes(payload);
        uint splitIndex = 0;
        for (uint i = 0; i < b.length; i++) {
            if (b[i] == bytes1(",")) {
                splitIndex = i;
                break;
            }
        }
        require(splitIndex > 0 && splitIndex < b.length - 1, "Invalid payload format");

        bytes memory part1 = new bytes(splitIndex);
        bytes memory part2 = new bytes(b.length - splitIndex - 1);
        for (uint j = 0; j < splitIndex; j++) part1[j] = b[j];
        for (uint j = splitIndex + 1; j < b.length; j++) part2[j - splitIndex - 1] = b[j];

        string memory idString = _trim(string(part1));
        uint drugId = _stringToUint(idString);
        address newOwner = _parseAddress(_trim(string(part2)));
        return (drugId, newOwner);
    }

    function _stringToUint(string memory s) internal pure returns (uint result) {
        bytes memory b = bytes(s);
        for (uint i = 0; i < b.length; i++) {
            if (b[i] == 0x20) continue; // skip space
            require(b[i] >= 0x30 && b[i] <= 0x39, "Invalid uint string");
            result = result * 10 + (uint(uint8(b[i])) - 48);
        }
    }

    function _parseAddress(string memory s) internal pure returns (address) {
        bytes memory tmp = bytes(s);
        require(tmp.length == 42, "Invalid address length");
        uint160 iaddr = 0;
        uint160 b1;
        uint160 b2;
        for (uint i = 2; i < 42; i += 2) {
            iaddr *= 256;
            b1 = uint160(uint8(tmp[i]));
            b2 = uint160(uint8(tmp[i + 1]));
            b1 = _fromHexChar(b1);
            b2 = _fromHexChar(b2);
            iaddr += (b1 * 16 + b2);
        }
        return address(iaddr);
    }

    function _fromHexChar(uint160 c) internal pure returns (uint160) {
        if (c >= 97) return c - 87;
        if (c >= 65) return c - 55;
        return c - 48;
    }

    function _trim(string memory str) internal pure returns (string memory) {
        bytes memory b = bytes(str);
        uint start = 0;
        uint end = b.length;

        while (start < end && b[start] == 0x20) start++;
        while (end > start && b[end - 1] == 0x20) end--;

        bytes memory trimmed = new bytes(end - start);
        for (uint i = start; i < end; i++) {
            trimmed[i - start] = b[i];
        }
        return string(trimmed);
    }

    function getCurrentOwner(uint drugId) public view returns (address) {
        return drugs[drugId].currentOwner;
    }
}




