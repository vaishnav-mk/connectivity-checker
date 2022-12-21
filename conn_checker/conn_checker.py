import asyncio
import pprint
import aiohttp

from http.client import HTTPConnection
from urllib.parse import urlparse
from datetime import datetime


async def ping_url(url, timeout=5):
    """This function pings a URL and returns True if it is reachable"""
    error = Exception("Unknown error")
    parsed_url = urlparse(url)
    host = parsed_url.netloc or parsed_url.path.split("/")[0]
    res = {
        "success": False,
        "reason": None,
    }
    for scheme in ["http", "https"]:
        target = f"{scheme}://{host}"
        try:
            async with aiohttp.ClientSession() as session:
                start_time = datetime.now()
                async with session.head(target, timeout=timeout) as response:
                    end_time = datetime.now()
                    res = {
                        "url": url,
                        "status": response.status,
                        "success": response.status == 200,
                        "reason": response.reason,
                        "time": {
                            "seconds": (end_time - start_time).total_seconds(),
                            "start_time": start_time.strftime("%H:%M:%S.%f"),
                            "end_time": end_time.strftime("%H:%M:%S.%f"),
                        },
                    }
        except asyncio.TimeoutError:
            res["reason"] = "Timeout error"
            error = Exception("Timeout error")
        except Exception as e:
            if "getaddrinfo failed" in str(e):
                res["reason"] = "DNS resolution error"
                error = Exception("DNS resolution error")
            res["reason"] = str(e)
            error = e
        finally:
            return res
    raise error


def ping_url_sync(url, timeout=5):
    """This function pings a URL and returns True if it is reachable"""
    error = Exception("Unknown error")
    parsed_url = urlparse(url)
    host = parsed_url.netloc or parsed_url.path.split("/")[0]
    res = {
        "success": False,
        "reason": None,
    }
    for port in [80, 443]:
        try:
            start_time = datetime.now()
            connection = HTTPConnection(host, port, timeout=timeout)
            connection.request("HEAD", "/")
            response = connection.getresponse()
            end_time = datetime.now()
            res = {
                "url": url,
                "status": response.status,
                "success": response.status == 200,
                "reason": response.reason,
                "time": {
                    "seconds": (end_time - start_time).total_seconds(),
                    "microseconds": (end_time - start_time).total_seconds() * 1000000,
                    "start_time": start_time.strftime("%H:%M:%S.%f"),
                    "end_time": end_time.strftime("%H:%M:%S.%f"),
                },
            }

        except Exception as e:
            if "getaddrinfo failed" in str(e):
                res["reason"] = "Invalid URL"
                error = Exception("Invalid URL")
            elif "timed out" in str(e):
                res["reason"] = "Timeout error"
                error = Exception("Timeout error")
            else:
                res["reason"] = "Unknown error"
                error = e
        finally:
            connection.close()
            return res
    raise error
