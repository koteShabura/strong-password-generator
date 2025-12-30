#!/usr/bin/env python3
"""
Strong Password Generator CLI Tool
Author: Kote Shaburishvili
Version: 2.0
"""

import secrets
import string
import sys
import argparse
from pathlib import Path

def get_yes_no(prompt, default=True):
    """Get yes/no input with default value"""
    default_str = "[Y/n]" if default else "[y/N]"
    while True:
        print(f"\n{prompt} {default_str}")
        choice = input(" >> ").strip().lower()
        if choice == "":
            return default
        if choice in ["y", "yes", "1"]:
            return True
        if choice in ["n", "no", "2"]:
            return False
        print("Invalid input. Enter y/n or press Enter for default.")

def get_length(min_len=8, max_len=128):
    """Get password length with validation"""
    while True:
        try:
            length = input(f"\nEnter password length ({min_len}–{max_len}, default 16): ").strip()
            if length == "":
                return 16
            length = int(length)
            if min_len <= length <= max_len:
                return length
            print(f"Length must be between {min_len} and {max_len}.")
        except ValueError:
            print("Invalid input. Enter a number.")

def get_count():
    """Get number of passwords to generate"""
    while True:
        try:
            count = input("\nHow many passwords to generate? (1-20, default 1): ").strip()
            if count == "":
                return 1
            count = int(count)
            if 1 <= count <= 20:
                return count
            print("Count must be between 1 and 20.")
        except ValueError:
            print("Invalid input. Enter a number.")

def calculate_strength(length, charset_size):
    """Calculate password strength rating"""
    import math
    entropy = length * math.log2(charset_size)
    if entropy < 50:
        return "WEAK ⚠️"
    elif entropy < 75:
        return "MEDIUM 🔶"
    else:
        return "STRONG ✓"

def generate_password(length, use_symbols, use_numbers, exclude_ambiguous=False):
    """Generate a cryptographically secure password"""
    chars = string.ascii_letters
    
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if exclude_ambiguous:
        ambiguous = "il1Lo0O"
        chars = "".join(c for c in chars if c not in ambiguous)
    
    if not chars:
        raise ValueError("No characters available")
    
    password = "".join(secrets.choice(chars) for _ in range(length))
    
    # Ensure at least one from each category
    if use_numbers and not any(c in string.digits for c in password):
        password = password[:-1] + secrets.choice(string.digits)
    if use_symbols and not any(c in string.punctuation for c in password):
        password = password[:-1] + secrets.choice(string.punctuation)
    
    return password

def copy_to_clipboard(text):
    """Try to copy to clipboard"""
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        return False

def save_to_file(passwords, filename="passwords.txt"):
    """Save passwords to file"""
    try:
        path = Path(filename)
        with path.open("a") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False

def interactive_mode():
    """Run interactive mode"""
    print("╔═══════════════════════════════════════╗")
    print("║   STRONG PASSWORD GENERATOR v2.0      ║")
    print("╚═══════════════════════════════════════╝")
    
    use_symbols = get_yes_no("Include symbols?", default=True)
    use_numbers = get_yes_no("Include numbers?", default=True)
    exclude_ambiguous = get_yes_no("Exclude ambiguous characters (il1Lo0O)?", default=False)
    length = get_length()
    count = get_count()
    
    # Calculate charset size
    charset_size = 52  # letters
    if use_numbers:
        charset_size += 10
    if use_symbols:
        charset_size += len(string.punctuation)
    if exclude_ambiguous:
        charset_size -= 7
    
    strength = calculate_strength(length, charset_size)
    
    print("\n" + "═"*50)
    print(f" GENERATED PASSWORD{'S' if count > 1 else ''} (Strength: {strength})")
    print("─"*50)
    
    passwords = []
    for i in range(count):
        password = generate_password(length, use_symbols, use_numbers, exclude_ambiguous)
        passwords.append(password)
        print(f"  {i+1}. {password}")
    
    print("═"*50 + "\n")
    
    # Options after generation
    if len(passwords) == 1:
        if get_yes_no("Copy to clipboard?", default=False):
            if copy_to_clipboard(passwords[0]):
                print("✓ Copied to clipboard!")
            else:
                print("⚠ Install pyperclip for clipboard: pip3 install pyperclip")
    
    if get_yes_no("Save to file?", default=False):
        filename = input("Filename (default: passwords.txt): ").strip() or "passwords.txt"
        if save_to_file(passwords, filename):
            print(f"✓ Saved to {filename}")

def cli_mode(args):
    """Run CLI mode"""
    for i in range(args.count):
        password = generate_password(
            args.length,
            args.symbols,
            args.numbers,
            args.exclude_ambiguous
        )
        print(password)
        
        if args.save:
            save_to_file([password], args.save)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate strong, cryptographically secure passwords",
        epilog="Run without arguments for interactive mode"
    )
    parser.add_argument("-l", "--length", type=int, default=16,
                       help="Password length (default: 16)")
    parser.add_argument("-c", "--count", type=int, default=1,
                       help="Number of passwords (default: 1)")
    parser.add_argument("-s", "--symbols", action="store_true",
                       help="Include symbols")
    parser.add_argument("-n", "--numbers", action="store_true",
                       help="Include numbers")
    parser.add_argument("-x", "--exclude-ambiguous", action="store_true",
                       help="Exclude ambiguous chars (il1Lo0O)")
    parser.add_argument("--save", type=str, metavar="FILE",
                       help="Save to file")
    parser.add_argument("--version", action="version", version="%(prog)s 2.0")
    
    args = parser.parse_args()
    
    # No arguments = interactive mode
    if len(sys.argv) == 1:
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
    else:
        cli_mode(args)

if __name__ == "__main__":
    main()