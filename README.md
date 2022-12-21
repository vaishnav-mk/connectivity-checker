# connectivity-checker
🔌 A simple CLI tool to check the connectivity of one or more sites!

## TODO
* [ ] Add support for multiple files
* [ ] Add support for multiple timeouts
* [ ] Add flag for verbose output
* [ ] Add flag for single URL
* [ ] Add API support

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

    -m, --multi <url>      Multiple URLs to check (separated by a comma)
    -f, --file <file>      The file containing the URLs to check
    -t, --timeout <time>   The timeout in milliseconds (default: 5000)
    -h, --help             output usage information
```

## Examples

```bash
$ connectivity-checker -f urls.txt
$ connectivity-checker -m https://google.com -t 10000
$ connectivity-checker -m https://google.com,https://github.com
```
## Used packages
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
* [argparse](https://docs.python.org/3/library/argparse.html)
