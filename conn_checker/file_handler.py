import pathlib
import sys


def read_file(file):
    file_path = pathlib.Path(file)
    if file_path.exists():
        with open(file_path, "r") as f:
            urls = f.read().splitlines()
            if urls:
                return urls
            else:
                print(f"File {file_path} is empty")
                sys.exit(1)
    else:
        print(f"File {file_path} does not exist")
        sys.exit(1)
