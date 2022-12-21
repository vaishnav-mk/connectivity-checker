import re


def url_validator(urls=[]):
    """Validate URL"""

    valid_urls = []

    regex = re.compile(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    )

    for url in urls:
        if regex.match(url):
            valid_urls.append(url)
        else:
            print(f"Invalid URL: {url}")
    return valid_urls
