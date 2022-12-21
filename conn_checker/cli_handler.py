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
        "-su",
        "--success",
        help="Display only successful connections",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--files",
        metavar="files",
        help="Check connectivity of websites from one or more files",
        type=str,
        default=[],
        nargs="+",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        metavar="timeout",
        help="Set timeout for connection",
        type=int,
        default=[5],
        nargs="+",
    )
    parser.add_argument(
        "-u",
        "--url",
        metavar="url",
        help="Check connectivity of a single website",
        type=str,
        default="",
    )

    return parser.parse_args()