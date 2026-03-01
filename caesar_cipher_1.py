#!/usr/bin/env python3
"""
caesar_cipher.py - Caesar Cipher for password protection.

Encrypts a password by shifting each character by a fixed key.
Does NOT use any cryptographic libraries.

SRS 1 - Mobile Application Security
"""

SHIFT_KEY = 7       # shift key (can be changed from 1 to 126)
CHARSET_SIZE = 128  # ASCII table size


def caesar_encrypt(password: str, shift: int = SHIFT_KEY) -> str:
    """Encrypt a string by shifting each character by shift positions."""
    encrypted = ""
    for char in password:
        shifted_code = (ord(char) + shift) % CHARSET_SIZE
        encrypted += chr(shifted_code)
    return encrypted


def caesar_decrypt(cipher_text: str, shift: int = SHIFT_KEY) -> str:
    """Decrypt a string by shifting each character back by shift positions."""
    decrypted = ""
    for char in cipher_text:
        original_code = (ord(char) - shift) % CHARSET_SIZE
        decrypted += chr(original_code)
    return decrypted


def main() -> None:
    """Entry point: ask for password, encrypt and decrypt it."""
    print("=" * 45)
    print("   Caesar Cipher - Password Protection")
    print("=" * 45)

    password = input("\nEnter password: ")

    encrypted = caesar_encrypt(password)
    print(f"\nOriginal password  : {password}")
    print(f"Encrypted password : {encrypted}")

    decrypted = caesar_decrypt(encrypted)
    print(f"Decrypted password : {decrypted}")
    print(f"\nVerification (match?): {password == decrypted}")
    print("=" * 45)


if __name__ == "__main__":
    main()
