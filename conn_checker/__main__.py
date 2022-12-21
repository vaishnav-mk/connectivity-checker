""""Entry point for the application script"""

import asyncio
import pathlib
import sys

from conn_checker import cli_handler, conn_checker, file_handler


def main():
    """ "The core of the application"""
    args = cli_handler.handle_cli()
    print(args)

    if args.file:
        urls = file_handler.read_file(args.file)
    elif args.multi:
        urls = args.multi
    else:
        urls = [input("Enter a URL: ")]

    if args.asynchronous:
        for url in urls:
            try:
                result = asyncio.run(conn_checker.ping_url(url, args.timeout))
                display_results(result, url)
            except Exception as e:
                display_results(None, url, error=e)
    else:
        for url in urls:
            try:
                result = conn_checker.ping_url_sync(url, args.timeout)
                print(result)
                display_results(result, url)
            except Exception as e:
                display_results(None, url, error=e)


def display_results(result, url, error=None):
    """Display results of the connectivity check"""
    print(f"The status of {url} is", end=" ")
    if result:
        print(result)
    else:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
