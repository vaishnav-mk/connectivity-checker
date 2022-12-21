import datetime
from fastapi import FastAPI

app = FastAPI()


def default_response(msg = "Welcome to the connection checker API! (go to /docs to see what endpoints are available)", success=True, **kwargs):
    return {
        "success": success,
        "time": datetime.datetime.now().strftime("%H:%M:%S.%f"),
        "message": msg,
        **kwargs,
    }


@app.get("/")
async def root():
    return default_response()


@app.get("/ping")
async def ping():
    return default_response(msg="pong")

@app.post("/validate")
async def validate(urls: list):
    validated_urls = validate_urls(urls) or []
    return default_response(msg="Validated URLs", validated_urls=validated_urls)


@app.post("/connectioncheck")
async def check(urls: list, timeout: list = [5]):
    validated_urls = validate_urls(urls) or []
    if not validated_urls:
        return default_response(msg="No URLs to check", success=False)
    results = await check_urls(validated_urls, timeout)
    return default_response(msg="Checked URLs", results=results)
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
