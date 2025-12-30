#!/usr/bin/env python3
"""
Strong Password Generator CLI Tool
Author: Kote Shaburishvili
"""

import secrets
import string

def get_yes_no(prompt):
    print(prompt)
    print("[1] Yes")
    print("[2] No")
    choice = input("> ").strip()
    return choice == "1"

def get_length():
    while True:
        try:
            length = int(input("How many characters do you want? (1–50)\n> "))
            if 1 <= length <= 50:
                return length
            else:
                print("Please choose a number between 1 and 50.")
        except ValueError:
            print("Invalid input. Enter a number.")

def generate_password(length, use_symbols):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    print("=== Strong Password Generator ===\n")
    use_symbols = get_yes_no("Do you want the password to contain symbols?")
    length = get_length()
    password = generate_password(length, use_symbols)

    print("\nHere is a strong, randomly generated password:")
    print(password)

if __name__ == "__main__":
    main()
