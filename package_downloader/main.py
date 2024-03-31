from .app import downloader


def run():
    print("Welcome to Package Downloader\n")

    url: str = input("Enter a url of Resource: ")
    name: str = input("Enter a name of Resource: ")

    if name.endswith(".exe"):
        print("Are you sure you want download a exe from the url...")
        print("Please check for any virus, \
              they might or might not be there in exe...")
        if input("press y to continue downloading: ").lower() != "y":
            print("Thanks for using Package Downloader!!!!")
            return

    result = downloader.download(url, name)

    print("Resource is saved successfully!!: " + result)
