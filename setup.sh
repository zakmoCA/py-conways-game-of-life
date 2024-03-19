#!/bin/bash

REQUIRED_PYTHON_MAJOR=3
REQUIRED_PYTHON_MINOR=11

PYTHON_VERSION=$(python3 -c "import sys; print(sys.version_info[:2])")
EXPECTED_VERSION="($REQUIRED_PYTHON_MAJOR, $REQUIRED_PYTHON_MINOR)"

if [ "$PYTHON_VERSION" \< "$EXPECTED_VERSION" ]; then
    echo "Python version must be $REQUIRED_PYTHON_MAJOR.$REQUIRED_PYTHON_MINOR or higher. Please install or update Python."
    exit 1
fi

# remove any existing virtual environment to prevent headaches
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

echo "Sit tight while I create a new virtual environment..."
python3 -m venv venv || { echo "Failed to create virtual environment"; exit 1; }

source venv/bin/activate

echo "Now upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

echo "Setup complete.'"

# run game
python3 main.py

echo "Setup complete. Here are the game controls:"
echo "SPACE: Start/Pause the game."
echo "Mouse Click: Add/Remove cells."
echo "C: Clear the grid."
echo "R: Randomly populate the grid."
echo "You're in business! Launching the game..."