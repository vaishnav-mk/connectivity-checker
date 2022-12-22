import validators
import aiohttp


def validate_urls(urls):
    validated_urls = []
    for url in urls:
        if validators.url(url):
            validated_urls.append(url)
    return validated_urls


async def check_urls(urls, timeout: list):
    results = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            results.append(await send_request(session, url, timeout[0]))
    return results


async def send_request(session: aiohttp.ClientSession, url: str, timeout: int):
    try:
        async with session.get(url, timeout=timeout) as response:
            return {
                "url": url,
                "status": response.status,
                "reason": response.reason,
                "headers": dict(response.headers),
            }
    except Exception as e:
        return {"url": url, "error": str(e)}
