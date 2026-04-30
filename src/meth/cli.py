import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog="Meth", description="Replaces USELESS math module"
    )

    parser.add_argument(
        "-d",
        "--dir",
        default=".",
        type=str,
        help="path for directory to be recursively scanned for BLASPHEMOUS code",
    )

    return parser.parse_args()
