import requests  # type: ignore


def download(url: str, name: str) -> str:
    res = requests.get(url, stream=True)
    contentLength = res.headers["Content-Length"]

    print("Size of Content is:", contentLength)

    with open(name, "wb") as f:
        for chunk in res.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)

    print("Download Successfully!!!")

    return "./" + name
