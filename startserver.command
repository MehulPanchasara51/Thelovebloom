#!/bin/bash

# Move into the directory where this script is located
cd "$(dirname "$0")"

PORT=8000

# Try using PHP first (doesn't require Xcode tools)
if command -v php >/dev/null 2>&1; then
    (sleep 1 && open "http://localhost:$PORT/index.html") &
    echo "Starting local server using PHP on port $PORT..."
    php -S localhost:$PORT
else
    # Ultimate fallback: If no server tools work, just open the file directly in the browser
    echo "No local server tools available. Opening file directly..."
    open "index.html"
fi