# Strong Password Generator

A simple, secure password generator for Linux terminal. Creates cryptographically strong passwords using Python's secrets module.

## Installation

```bash
git clone https://github.com/yourusername/strong-password-generator.git
cd strong-password-generator
chmod +x install.sh
./install.sh
source ~/.bashrc
```

## Usage

### Interactive Mode

```bash
passgen
```

### CLI Mode

```bash
# Basic password with symbols and numbers
passgen -l 16 -s -n

# Generate 5 passwords
passgen -l 20 -s -n -c 5

# Save to file
passgen -l 16 -s -n --save passwords.txt

# Exclude ambiguous characters (il1Lo0O)
passgen -l 20 -s -n -x

# Check password strength
passgen --check "MyPassword123!"

# Use presets for common scenarios
passgen --preset wifi
passgen --preset strong
passgen --preset pin
```

### Presets

Quick shortcuts for common password types:

```bash
passgen --preset wifi      # 16 chars, no ambiguous (easy to type on phone)
passgen --preset strong    # 24 chars, maximum security
passgen --preset pin       # 6 digit PIN
passgen --preset basic     # 12 chars, letters + numbers
passgen --preset max       # 32 chars, ultra secure
```

### Options

```
-l, --length          Password length (default: 16)
-c, --count          Number of passwords (default: 1)
-s, --symbols        Include symbols
-n, --numbers        Include numbers
-x, --exclude-ambiguous   Exclude il1Lo0O
--save FILE          Save to file
--check PASSWORD     Analyze password strength
--preset TYPE        Use preset (wifi, strong, pin, basic, max)
--help               Show help
```

## License

MIT License

## Author

Kote Shaburishvili