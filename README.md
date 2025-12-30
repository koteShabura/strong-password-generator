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
```

### Options

```
-l, --length          Password length (default: 16)
-c, --count          Number of passwords (default: 1)
-s, --symbols        Include symbols
-n, --numbers        Include numbers
-x, --exclude-ambiguous   Exclude il1Lo0O
--save FILE          Save to file
--help               Show help
```

## License

MIT License

## Author

Kote Shaburishvili