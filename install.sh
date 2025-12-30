#!/bin/bash

# Simple installer for strong-password-generator
# Author: Kote Shaburishvili

echo "Installing Strong Password Generator..."

# Make script executable
chmod +x passgen.py

# Copy to /usr/local/bin for global access
sudo cp passgen.py /usr/local/bin/passgen

echo "Installation complete!"
echo "You can now run the tool with: passgen"
