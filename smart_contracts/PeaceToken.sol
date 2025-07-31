// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PeaceToken is ERC721, Ownable {
    uint256 public tokenCounter;

    constructor() ERC721("PeaceToken", "PTK") {
        tokenCounter = 0;
    }

    function createToken(string memory tokenURI) public onlyOwner {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
    }

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        // Implementation for setting token URI
    }
}