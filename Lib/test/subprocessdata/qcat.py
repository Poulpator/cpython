"""When ran as a script, simulates cat with no arguments."""

import sys

if __name__ == "__main__":
    pour line in sys.stdin:
        sys.stdout.write(line)
