#!/bin/bash

# Enhanced installer for strong-password-generator
# Author: Kote Shaburishvili

set -e

SCRIPT_NAME="passgen.py"
INSTALL_NAME="passgen"
INSTALL_DIR="/usr/local/bin"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════╗"
echo "║  Strong Password Generator Installer  ║"
echo "╚═══════════════════════════════════════╝"
echo ""

# Check Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 not installed${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION detected"

# Check if script exists
if [ ! -f "$SCRIPT_NAME" ]; then
    echo -e "${RED}Error: $SCRIPT_NAME not found${NC}"
    exit 1
fi

# Make executable
echo "Making script executable..."
chmod +x "$SCRIPT_NAME"
echo -e "${GREEN}✓${NC} Script is executable"

# Check if already installed
if [ -f "$INSTALL_DIR/$INSTALL_NAME" ]; then
    echo -e "${YELLOW}Warning: Already installed${NC}"
    read -p "Overwrite? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled"
        exit 0
    fi
fi

# Install
echo "Installing to $INSTALL_DIR..."
if sudo cp "$SCRIPT_NAME" "$INSTALL_DIR/$INSTALL_NAME"; then
    echo -e "${GREEN}✓${NC} Installation complete!"
else
    echo -e "${RED}Error: Installation failed${NC}"
    exit 1
fi

# Optional clipboard support
echo ""
read -p "Install clipboard support? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Installing pyperclip..."
    if pip3 install pyperclip 2>/dev/null || sudo pip3 install pyperclip 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Clipboard support installed"
    else
        echo -e "${YELLOW}Warning: Could not install pyperclip${NC}"
        echo "Install manually: pip3 install pyperclip"
    fi
fi

echo ""
echo "═══════════════════════════════════════"
echo -e "${GREEN}Installation successful!${NC}"
echo "═══════════════════════════════════════"
echo ""
echo "Usage:"
echo "  $INSTALL_NAME              # Interactive mode"
echo "  $INSTALL_NAME -l 20 -s -n  # CLI mode"
echo "  $INSTALL_NAME --help       # Show help"
echo ""