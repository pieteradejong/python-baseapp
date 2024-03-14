#!/bin/bash

# create Python virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# echo "Initialization complete!"
echo
echo -e "\033[0;32mInitialization complete!\033[0m"
