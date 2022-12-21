""""Entry point for the application script"""

import asyncio
import sys

from cli import cli_handler, file_handler, validate_urls, conn_checker, result_handler

def main():
    """The core of the application"""


    args = cli_handler.handle_cli()
    urls = []
    results = []

    # get urls from file or from cli
    if args.files:
        urls = file_handler.read_files(args.files)
    elif args.multi:
        urls = args.multi
    elif args.url:
        urls = [args.url]

    # validate urls and remove duplicates
    urls = list(dict.fromkeys(validate_urls.url_validator(urls)))

    if not urls:
        print("Exiting: No URLs to check")
        sys.exit(1)

    # timeout for each url (in seconds) - default is 5 seconds per url 
    timeout = args.timeout * len(urls)

    # check connectivity
    for index, url in enumerate(urls):
        pinger = conn_checker.PingURL(url, timeout[index])
        try:
            if args.asynchronous:
                result = asyncio.run(pinger.ping_async())
                results.append({"url": url, "result": result})
            else:
                result = pinger.ping_sync()
                results.append({"url": url, "result": result})
        except Exception as e:
            results.append({"url": url, "result": None, "error": e})

    # display results
    result_display = result_handler.DisplayResults(results, args)
    result_display.display_results()

if __name__ == "__main__":
    main()
