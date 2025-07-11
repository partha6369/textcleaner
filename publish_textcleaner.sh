#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Step 1: Cleaning previous builds..."
rm -rf dist build textcleaner_partha.egg-info
if [ $? -eq 0 ]; then
    echo "✅ Cleaned old build directories."
else
    echo "❌ Failed to clean old builds." >&2
    exit 1
fi

echo "Step 2: Building new package..."
python setup.py sdist bdist_wheel
if [ $? -eq 0 ]; then
    echo "✅ Package built successfully."
else
    echo "❌ Build failed." >&2
    exit 1
fi

echo "Step 3: Uploading to PyPI..."
twine upload dist/*
if [ $? -eq 0 ]; then
    echo "✅ Upload completed successfully."
else
    echo "❌ Upload failed. Check error message above." >&2
    exit 1
fi

echo "🎉 All steps completed successfully!"
