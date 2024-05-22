
# Caesar Cipher

# Simple but Weak: Caesar Cipher Algorithm

This repository contains implementations of the Caesar Cipher algorithm in Python. The Caesar Cipher is a straightforward encryption technique, historically used by Julius Caesar, which shifts the letters in the plaintext by a fixed number of positions down the alphabet.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

The Caesar Cipher is one of the earliest and simplest methods of encryption. Despite its historical significance, it is easily broken and thus considered weak by modern cryptographic standards. This project provides a practical implementation of the Caesar Cipher and includes functions for both encryption and decryption.

## Features

- Encrypt text using the Caesar Cipher.
- Decrypt text encrypted with the Caesar Cipher.
- Handle both uppercase and lowercase letters.
- Ignore non-alphabetic characters during encryption and decryption.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/zeynepclktn/CaesarCipher
    ```
2. Navigate to the project directory:
    ```sh
    cd caesar-cipher-algorithm
    ```

## Usage

You can use the provided Python functions to encrypt and decrypt messages using the Caesar Cipher.

### Encrypting Text

The `encrypt` function shifts the characters in the text by a specified number of positions.

### Decrypting Text
The `decrypt` function reverses the shift applied during encryption.

### Encrypting Text with ASCII Values
The `encryptascii` function shifts the characters in the text using ASCII values.

### Decrypting Text with ASCII Values
The `decryptascii` function reverses the shift applied during ASCII-based encryption.

### Encrypting Text with ASCII Values + Upper-LowerCase
The `encryptupperlower` function decrypts text encrypted using the Caesar Cipher algorithm, maintaining the case of the letters.

### Decrypting Text with ASCII Values + Upper-LowerCase
The `decryptupperlower` function decrypts text encrypted using the Caesar Cipher algorithm, maintaining the case of the letters.
