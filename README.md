Message Encryption and Decryption Tool

This project is a Python-based application with a graphical user interface (GUI) for encrypting and decrypting messages using a substitution cipher technique. It is developed using the Tkinter library for the interface and base64 for encoding the message.
## Table of Contents

- Features
- How it Works
- Installation
-  Usage
-  equirements
- Screenshot
- License
- Author

## Features

  - Encrypt Messages: Encrypt a message using a user-defined key.
  - Decrypt Messages: Decrypt encrypted messages with the same key.
  - Simple GUI: Easy-to-use interface built with Tkinter.
  - ustom Key: Input any integer as the encryption/decryption key.
  - Switch Between Modes: Use 'e' for encryption and 'd' for decryption.

## How it Works

 - Encryption:
        - The message is encoded character by character based on the key. Each character's Unicode value is shifted using the corresponding character from the key.
       -  The encoded string is further converted to a base64 string for extra security.
  -  Decryption:
       -  The process reverses, decoding the base64 string and then shifting each character back using the same key.
