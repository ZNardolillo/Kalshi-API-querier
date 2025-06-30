import requests

# request the target  URL
def crawler():
    #Lets someone enter the url with or without the https:// portion
    url = input("Enter url to crawl")
    try:
        response = requests.get(url)
    except:
        response = requests.get("https://"+url)

    #I think this fetches the page's raw html or something
    response.raise_for_status()

    print(response.text)

crawler()