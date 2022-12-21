""""Entry point for the application script"""

import asyncio
import sys
import re

from conn_checker import cli_handler, conn_checker, file_handler

def url_validator(urls = []):
    """Validate URL"""


    valid_urls = []
    
    regex = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
    
    for url in urls:
        if regex.match(url):
            valid_urls.append(url)
        else:
            print(f"Invalid URL: {url}")
    return valid_urls

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

    # validate urls
    urls = url_validator(urls)

    if not urls:
        print("Exiting: No URLs to check")
        sys.exit(1)

    # timeout for each url (in seconds) - default is 5 seconds per url 
    timeout = args.timeout * len(urls)

    # check connectivity
    if args.asynchronous:
        for index, url in enumerate(urls):
            try:
                result = asyncio.run(conn_checker.ping_url(url, timeout[index]))
                results.append({"url": url, "result": result})
            except Exception as e:
                results.append({"url": url, "result": None, "error": e})
    else:
        for index, url in enumerate(urls):
            try:
                result = conn_checker.ping_url_sync(url, timeout[index])
                results.append({"url": url, "result": result})
            except Exception as e:
                results.append({"url": url, "result": None, "error": e})
    
    display_results(results, args)

def display_results(results, args):
    """Display results of the connectivity check"""

    verbose = args.verbose
    success = []
    failure = []

    print(f"Results ({len(results)}):")
    print("--------------------")

    for result in results:
        if result["result"]["success"]:
            success.append(result)
        else:
            failure.append(result)
    
    if args.success:
        if not success:
            print(f"No successful connections found for {len(results)} URLs")
        for result in success:
            verbose_results(results) if verbose else print(f"Success: {result['url']}")
    else:
        if verbose:
            verbose_results(results)
        else:
            for index, result in enumerate(results):
                print("[{}] {}: {}".format(index+1, "success" if success else "No", result['url']))
            


def verbose_results(results):
    for index, result in enumerate(results):
        print(f"[{index+1}] URL: {result['url']}")
        print(f"Success: {result['result']['success']}")
        for key, value in result["result"].items():
            if ["success", "url"].count(key) > 0:
                continue
            elif key == "error":
                print(f"Error: {value}")
            elif key == "time":
                print("Time taken: {0:.2f} seconds".format(value["seconds"]))
            else:
                print(f"{key}: {value}")
        print("--------------------")

if __name__ == "__main__":
    main()
