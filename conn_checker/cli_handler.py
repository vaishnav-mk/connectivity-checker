"""Command line Interface handler"""

import argparse


def handle_cli():
    parser = argparse.ArgumentParser(
        prog="connectivity-checker",
        description="Tool to check connectivity of websites",
        epilog="This tool is used to check connectivity of websites",
    )
    parser.add_argument(
        "-m",
        "--multi",
        metavar="multi_urls",
        nargs="+",
        help="Check connectivity of multiple websites instead of one",
        type=str,
        default=[],
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        help="Check connectivity of websites asynchronously (can be slow)",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="file",
        help="Check connectivity of websites from a file",
        type=str,
        default="",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        metavar="timeout",
        help="Set timeout for connection",
        type=int,
        default=5,
    )
    return parser.parse_args()


def main():
    args = handle_cli()
    print(args)


main()
