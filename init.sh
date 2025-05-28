#!/bin/bash
set -e

# Colors for output
green='\033[0;32m'
red='\033[0;31m'
reset='\033[0m'

# Function to check Python version
check_python_version() {
    local min_version="3.12.0"
    if ! command -v python3.12 &> /dev/null; then
        echo -e "${red}❌ Python 3.12 is not installed. Please install it first.${reset}"
        echo -e "You can install it using:"
        echo -e "  - macOS: brew install python@3.12"
        echo -e "  - Linux: Use your distribution's package manager"
        exit 1
    fi
    
    local current_version=$(python3.12 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
    if [ "$(printf '%s\n' "$min_version" "$current_version" | sort -V | head -n1)" != "$min_version" ]; then
        echo -e "${red}❌ Python version 3.12 or higher is required. Current version: $current_version${reset}"
        exit 1
    fi
    echo -e "${green}✅ Python version $current_version is compatible${reset}"
}

# Check Python version first
check_python_version

# Remove Python virtual environment if it exists
echo -e "${green}🧹 Removing existing Python virtual environment (venv/) ...${reset}"
rm -rf venv

# Create new Python virtual environment with explicit Python version
echo -e "${green}🐍 Creating new Python virtual environment with Python 3.12 ...${reset}"
python3.12 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify Python version in virtual environment
venv_python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
if [[ ! "$venv_python_version" =~ ^3\.12\. ]]; then
    echo -e "${red}❌ Virtual environment Python version mismatch. Expected Python 3.12.x, got $venv_python_version${reset}"
    exit 1
fi
echo -e "${green}✅ Using Python $venv_python_version in virtual environment${reset}"

# Remove Python caches
echo -e "${green}🧹 Removing all __pycache__, .pytest_cache, and .ruff_cache directories ...${reset}"
find . -type d -name "__pycache__" -exec rm -rf {} +
rm -rf .pytest_cache .ruff_cache

# Install Python dependencies
echo -e "${green}📦 Installing Python dependencies ...${reset}"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Frontend setup if frontend/ exists
if [ -d "frontend" ]; then
    echo -e "${green}🧹 Cleaning frontend node_modules and dist ...${reset}"
    rm -rf frontend/node_modules frontend/dist
    
    echo -e "${green}📦 Installing frontend dependencies ...${reset}"
    cd frontend
    if [ -f "package-lock.json" ]; then
        npm install
    elif [ -f "yarn.lock" ]; then
        yarn install
    else
        echo -e "${red}No package-lock.json or yarn.lock found in frontend/. Skipping frontend install.${reset}"
    fi
    
    # Build or start frontend
    if grep -q '"build"' package.json; then
        echo -e "${green}🏗️  Building frontend ...${reset}"
        npm run build
    elif grep -q '"dev"' package.json; then
        echo -e "${green}🚀 Starting frontend dev server ...${reset}"
        npm run dev &
    else
        echo -e "${red}No build or dev script found in frontend/package.json. Skipping frontend start.${reset}"
    fi
    cd ..
fi

echo
if [ -d "frontend" ]; then
    echo -e "${green}✅ Initialization complete!${reset}"
    echo -e "${green}To activate the Python virtual environment: 'source venv/bin/activate'${reset}"
    echo -e "${green}To run the backend: './run.sh'${reset}"
    echo -e "${green}If the frontend dev server is running, visit: http://localhost:5173${reset}"
else
    echo -e "${green}✅ Initialization complete!${reset}"
    echo -e "${green}To activate the Python virtual environment: 'source venv/bin/activate'${reset}"
    echo -e "${green}To run the backend: './run.sh'${reset}"
fi
