"""Console script for tekton-neat."""
import os.path
import select
import argparse
import sys

from tekton_neat.tekton_neat import process


def main():
    """Console script for tekton-neat."""

    if select.select([sys.stdin], [], [], 0.0)[0]:
        print("\n".join(process(sys.stdin.read())))
        return 0
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    if not args.files:
        parser.print_help()
        return 1

    for filename in args.files:
        if not os.path.exists(filename):
            print(f"{filename} does not exist.")
            return 1
        print("\n".join(process(open(filename).read())))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
