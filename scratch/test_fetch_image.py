import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

test_url = "https://www.uchicago.asia/-/media/images/logo-background.svg"
req = urllib.request.Request(test_url, headers=headers)

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        data = resp.read()
        print(f"Success fetching {test_url}! Length: {len(data)} bytes")
except Exception as e:
    print(f"Failed fetching {test_url}: {e}")
