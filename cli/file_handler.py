import pathlib
import sys


def read_files(files):
    urls = []
    for file in files:
        urls += read_file(file)
    if not urls:
        print("No URLs to check")
        sys.exit(1)
    return urls

def read_file(file):
    file_path = pathlib.Path(file)
    if file_path.exists():
        with open(file_path, "r") as f:
            print("Reading file: ", file_path)
            text = f.read()
            if len(text) > 0:
                urls = text.splitlines()
                print(f"Found {len(urls)} URL(s)")
                return urls
            else:
                print(f"File: ({file_path}) is empty")
                return []
    else:
        print(f"File: ({file_path}) does not exist")
        sys.exit(1)