# Strong Password Generator

A cryptographically secure password generator for Linux terminal.

## Features

✓ Cryptographically secure (uses Python's `secrets` module)  
✓ Interactive mode with easy prompts  
✓ CLI mode for scripting  
✓ Password strength indicator  
✓ Generate multiple passwords at once  
✓ Clipboard support (optional)  
✓ Save to file  
✓ Exclude ambiguous characters option  

## Installation

```bash
chmod +x install.sh
./install.sh
```

## Usage

### Interactive Mode
```bash
passgen
```

### CLI Mode
```bash
# Generate 16-char password with symbols & numbers
passgen -l 16 -s -n

# Generate 5 passwords
passgen -l 20 -s -n -c 5

# Exclude ambiguous characters (il1Lo0O)
passgen -l 20 -s -n -x

# Save to file
passgen -l 16 -s -n --save passwords.txt
```

## Options

```
-l, --length LENGTH        Password length (default: 16)
-c, --count COUNT         Number of passwords (default: 1)
-s, --symbols             Include symbols
-n, --numbers             Include numbers
-x, --exclude-ambiguous   Exclude il1Lo0O characters
--save FILE               Save to file
--help                    Show help
--version                 Show version
```

## Examples

```bash
# Strong 24-character password
passgen -l 24 -s -n

# Simple password (letters only)
passgen -l 12

# Generate 10 passwords for a team
passgen -l 16 -s -n -c 10 --save team_passwords.txt

# Use in a script
API_KEY=$(passgen -l 32 -s -n)
```

## Security

- Uses `secrets` module for cryptographic strength
- Password strength ratings:
  - **WEAK ⚠️**: < 50 bits entropy
  - **MEDIUM 🔶**: 50-75 bits entropy  
  - **STRONG ✓**: > 75 bits entropy

## Requirements

- Python 3.6+
- Optional: `pyperclip` (for clipboard support)

```bash
pip3 install pyperclip
```

## Uninstall

```bash
sudo rm /usr/local/bin/passgen
```

## License

MIT License

## Author

Kote Shaburishvili

---

**Version 2.0** - Enhanced with CLI mode, strength indicator, and more features!