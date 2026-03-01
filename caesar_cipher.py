#!/usr/bin/env python3
"""
caesar_cipher.py — Шифр Цезаря для защиты пароля.

Шифрует пароль с ключом сдвига, умеет расшифровать обратно.
Не использует готовые криптографические библиотеки.

Автор: СРС 1 — Защита системы и данных в мобильных приложениях
"""

SHIFT_KEY = 7       # ключ сдвига (можно менять от 1 до 126)
CHARSET_SIZE = 128  # размер таблицы ASCII-символов


def caesar_encrypt(password: str, shift: int = SHIFT_KEY) -> str:
    """Зашифровать строку сдвигом каждого символа на shift позиций."""
    encrypted = ""
    for char in password:
        shifted_code = (ord(char) + shift) % CHARSET_SIZE
        encrypted += chr(shifted_code)
    return encrypted


def caesar_decrypt(cipher_text: str, shift: int = SHIFT_KEY) -> str:
    """Расшифровать строку обратным сдвигом (-shift)."""
    decrypted = ""
    for char in cipher_text:
        original_code = (ord(char) - shift) % CHARSET_SIZE
        decrypted += chr(original_code)
    return decrypted


def main() -> None:
    """Точка входа: запрашивает пароль, шифрует и дешифрует."""
    print("=" * 45)
    print("   Caesar Cipher — Защита пароля (СРС 1)")
    print("=" * 45)

    password = input("\nВведите пароль: ")

    encrypted = caesar_encrypt(password)
    print(f"\nОригинальный пароль  : {password}")
    print(f"Зашифрованный пароль : {encrypted}")

    decrypted = caesar_decrypt(encrypted)
    print(f"Расшифрованный пароль: {decrypted}")
    print(f"\nПроверка (совпадает?): {password == decrypted}")
    print("=" * 45)


if __name__ == "__main__":
    main()
