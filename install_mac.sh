#!/bin/bash

echo "Do you have a python interpreter (version 3)? (y/n) "

read input

if [ $input == 'n' ]; then
    echo "Installing Homebrew..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH
    echo "Installing the python interpreter..."
    brew install python3
fi

echo "Insalling pygame..."
pip3 install pygame
echo "Setting up window size..."
python3 set_size.py