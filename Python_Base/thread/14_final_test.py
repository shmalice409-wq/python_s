from concurrent.futures import ThreadPoolExecutor

import requests

MAX_WORKERS = 5
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}


def fetch(url):
    try:
        response = requests.get(url=url, headers=headers, timeout=3)
        return response.text
    except Exception as e:
        return f"url fail to request,{e}"


if __name__ == "__main__":
    url = ["https://llfc.club/", "https://gitbookcpp.llfc.club/"]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        result = pool.map(fetch, url)
        for r in result:
            print(r)
