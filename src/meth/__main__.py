"""
Entry point for the meth module when run from console.
"""

from .cli import parse
from .crusade import crusade


def main():
    """Main entry point for the meth command."""
    dir_path = parse().dir
    crusade(dir_path=dir_path)


if __name__ == "__main__":
    main()
