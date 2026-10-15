import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

test_urls = [
    "https://www.uchicago.edu/-/jssmedia/no-barriers-press-conf.jpg?w=280&h=280&iar=0",
    "https://www.uchicago.edu/-/jssmedia/odyssey-medals-400.jpg?w=280&h=280&iar=0",
    "https://www.uchicago.edu/-/jssmedia/uchicago-empower-400px.jpg?w=280&h=280&iar=0"
]

for u in test_urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = resp.read()
            print(f"Success fetching {u}! Size: {len(data)} bytes")
    except Exception as e:
        print(f"Failed {u}: {e}")
