#!/bin/bash

echo "🚀 Setting up Python virtual environment..."

# Go to backend app folder
cd app

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "✅ Backend setup complete!"
echo "⚡ To activate environment manually later, run: source venv/bin/activate"
