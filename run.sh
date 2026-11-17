#!/usr/bin/env bash
# Start the backend (:8000) and frontend (:5173) together. Ctrl+C stops both.
set -e
cd "$(dirname "$0")"

# Rebuild the storage engine if it's missing or engine.cpp changed since the last build
if [ ! -f cse/libcse.dylib ] || [ cse/engine.cpp -nt cse/libcse.dylib ]; then
    echo "Building cse/libcse.dylib..."
    c++ -std=c++17 -O2 -Wall -shared -fPIC -o cse/libcse.dylib cse/engine.cpp -lz
fi

[ -d frontend/node_modules ] || (cd frontend && bun install)

# On exit (Ctrl+C or either server dying), kill everything this script started
trap 'kill 0' EXIT

uv run fastapi dev server.py &
(cd frontend && bun run dev) &

wait -n  # return as soon as either server exits
