# connectivity-checker
🔌 A simple CLI tool to check the connectivity of one or more sites!

## TODO
* [x] Add support for multiple files
* [x] Add support for multiple timeouts
* [x] Add flag for verbose output
* [x] Add flag for single URL
* [ ] Add API support (working on it!)

## Installation

```bash
$ git clone github.com/vaishnav-mk/connectivity-checker
$ cd connectivity-checker
```

## Usage

```bash
$ connectivity-checker --help

  Usage: connectivity-checker [options]

  Options:

    -m, --multi <url>      Multiple URLs to check (separated by a whitespace)
    -f, --file <file>      The files containing the URLs to check
    -t, --timeout <time>   The timeouts in milliseconds (default: [5000])
    -h, --help             output usage information
    -u, --url <url>        The URL to check
    -v, --verbose          output the result of the check in verbose mode (default: false)
```

## Examples

```bash
$ connectivity-checker -f urls.txt more-urls.txt
$ connectivity-checker -u https://google.com -t 5 5 5 7
$ connectivity-checker -m https://google.com,https://github.com
$ connectivity-checker -u https://google.com -v
```

## Endpoints
* API Info:
* * API package used: [FastAPI](https://fastapi.tiangolo.com/)
* * Documentation: [Swagger](https://swagger.io/)
* * API docs: `/docs`

* API Endpoints:
* * Base URL: `127.0.0.1`
* * Port: `8000`
* * Docs: `/docs`

```bash
$ GET / - Returns the API info
$ GET /ping - Returns pong!
$ POST /check - Returns the statuses of an array of URLs
$ POST /validate - Returns valid URLs from an array of URLs
```
## Used packages
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [fastapi](https://fastapi.tiangolo.com/)
* [uvicorn](https://www.uvicorn.org/)
