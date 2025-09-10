#!/usr/bin/env bash
set -e  # exit immediately if a command fails

# Go to project root (script location)
cd "$(dirname "$0")"

# Activate virtual environment
if [ -f "venv/Scripts/activate" ]; then
    # Windows-style venv
    source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then
    # Unix/Linux/Mac-style venv
    source venv/bin/activate
else
    echo "❌ Could not find virtual environment in ./venv"
    exit 1
fi

# Run pytest
echo "▶️ Running test suite..."
pytest test_app.py
TEST_EXIT_CODE=$?

# Exit with 0 if tests passed, 1 otherwise
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed."
    exit 1
fi
