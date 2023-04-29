// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @custom:security-contact antonmarcelo@gmail.com
///Brazuca is the token name of the company with the certification
contract Brazuca is ERC20 {
    constructor() ERC20("Brazuca", "BZC") {
        _mint(msg.sender, 2000 * 10 ** decimals());
    }
}
