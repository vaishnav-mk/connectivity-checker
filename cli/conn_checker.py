import aiohttp
import asyncio

from http.client import HTTPConnection
from urllib.parse import urlparse
from datetime import datetime


class PingURL:
    def __init__(self, url, timeout=5):
        self.url = url
        self.timeout = timeout
        self.parsed_url = urlparse(url)
        self.host = self.parsed_url.netloc or self.parsed_url.path.split("/")[0]

    def build_result(self, response, start_time, end_time):
        return {
            "status": response.status if response else None,
            "success": response.status == 200 if response else False,
            "reason": response.reason if response else None,
            "time": {
                "seconds": (end_time - start_time).total_seconds(),
                "start_time": start_time.strftime("%H:%M:%S.%f"),
                "end_time": end_time.strftime("%H:%M:%S.%f"),
            },
        }

    async def ping_async(self):
        start_time = datetime.now()
        for scheme in ["http", "https"]:
            target = f"{scheme}://{self.host}"
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.head(target, timeout=self.timeout) as response:
                        return self.build_result(response, start_time, datetime.now())
            except Exception as e:
                res = self.build_result(None, start_time, datetime.now())
                res["reason"] = str(e)
        return res

    def ping_sync(self):
        start_time = datetime.now()
        for port in [80, 443]:
            try:
                connection = HTTPConnection(self.host, port, timeout=self.timeout)
                connection.request("HEAD", "/")
                response = connection.getresponse()
                connection.close()
                return self.build_result(response, start_time, datetime.now())
            except Exception as e:
                res = self.build_result(None, start_time, datetime.now())
                res["reason"] = str(e)
        return res
