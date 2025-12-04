import sys
from pathlib import Path

# Ensure project root is on sys.path so `from server import app` works
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from server import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
