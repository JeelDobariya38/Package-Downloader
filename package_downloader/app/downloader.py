import requests


def download(url: str, name: str) -> str:
    """## For download stuffs from internet.
    ---

    Args:
        url (str): url of resource (http/https).
        name (str): name to give to resourse after its downloading.

    Returns:
        str: path of resource.
    """
    res = requests.get(url, stream=True)
    contentLength = res.headers["Content-Length"]

    print("Size of Content is:", contentLength)

    with open(name, "wb") as f:
        for chunk in res.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)

    print("Download Successfully!!!")

    return "./" + name
