#!/bin/bash
# ==============================================================================
#  start-server.sh — Local dev server for LoveBloom
#  macOS equivalent of a .bat launcher
#
#  Usage:
#    1. Place this file in the SAME folder as index.html and carousel.json
#    2. Make it executable once:  chmod +x start-server.sh
#    3. Run it:                   ./start-server.sh   (or double-click in Finder)
#
#  Stops:  Press Ctrl+C in the terminal window
# ==============================================================================

PORT=8080

# Change into the directory that contains this script
# (works even if you run it from a different working directory)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "  🌸  LoveBloom — Local Server"
echo "  ──────────────────────────────────────"
echo "  Folder : $SCRIPT_DIR"
echo "  URL    : http://localhost:$PORT"
echo ""
echo "  Press Ctrl+C to stop the server."
echo ""

# ── Choose a server ───────────────────────────────────────────────────────────

start_server() {
  if command -v python3 &>/dev/null; then
    echo "  Using Python 3 http.server..."
    python3 -m http.server "$PORT"

  elif command -v python &>/dev/null; then
    PY_VER=$(python -c 'import sys; print(sys.version_info.major)')
    if [ "$PY_VER" = "3" ]; then
      echo "  Using Python 3 http.server..."
      python -m http.server "$PORT"
    else
      echo "  Using Python 2 SimpleHTTPServer..."
      python -m SimpleHTTPServer "$PORT"
    fi

  elif command -v npx &>/dev/null; then
    echo "  Python not found — falling back to npx serve..."
    npx serve -l "$PORT" .

  else
    echo "  ❌  No suitable server found."
    echo "  Please install Python 3 (https://python.org) or Node.js (https://nodejs.org)"
    exit 1
  fi
}

# ── Open browser after a short delay ─────────────────────────────────────────

(
  sleep 1.5
  open "http://localhost:$PORT/index.html"
) &

# ── Start blocking server ─────────────────────────────────────────────────────

start_server


