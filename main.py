# main.py

from fastapi import FastAPI, Body, HTTPException , status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse
import base64
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

short_urls = {}  # Dictionary to store short_code -> long URL mappings

# Function to generate a unique base64 encoded string
def generate_short_code():
    while True:
        random_bytes = random.getrandbits(64)
        encoded_url = base64.urlsafe_b64encode(random_bytes.to_bytes(8, byteorder='big')).decode()
        short_code = encoded_url[:6]  # Take first 6 characters
        if short_code not in short_urls:
            return short_code


def shorten_url_response(short_code):
    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "short_code": short_code
    }

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# API endpoint to shorten URLs
@app.post("/api/shorten")
async def shorten_url(url_data: dict = Body(...)):
    # handle no data exception
    if not url_data:
        raise HTTPException(status_code=400, detail="Missing URL data in request body")
    url = url_data.get("url")
    # handle no url exist in body exception
    if not url:
        raise HTTPException(status_code=400, detail="Missing 'url' field in request body")
    # handle invalid url exception
    if not validate_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL format")
    # check if url already exist and created shorted URL
    for short_code, long_url in short_urls.items():
        if long_url == url:
            return shorten_url_response(short_code)
    short_code = generate_short_code()
    short_urls[short_code] = url

    return shorten_url_response(short_code)


# Redirect route
@app.get("/{short_code}")
async def redirect_to_original(short_code: str):

    if short_code not in short_urls:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid short code")
    long_url = short_urls[short_code]
    return RedirectResponse(long_url, status_code=status.HTTP_302_FOUND)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)