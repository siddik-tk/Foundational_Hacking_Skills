import requests
from bs4 import BeautifulSoup

def printheadandcook(url):
    try:
        response = requests.get(url)
        print(f"\nStatus Code: {response.status_code}")

        print("\nResponse Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\nCookies:")
        for cookie in response.cookies:
            print(f"{cookie.name} = {cookie.value}")

    except Exception as e:
        print(f"\n Error: {e}")

def htmlpars(url):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        print("\nPage Title:")
        print(soup.title.string.strip() if soup.title else "No title tag")


        print("\n<meta> Tag Attributes:")
        for meta_tag in soup.find_all("meta"):
            print("Attributes:", meta_tag.attrs)


        print("\n<h1> Tags:")
        for h1_tag in soup.find_all("h1"):
            print(h1_tag.text.strip())


        print("\n<script> Tags:")
        for script_tag in soup.find_all("script"):
            print(script_tag)

    except Exception as e:
        print("error:"+e)


url = input("Enter the URL: ")
printheadandcook(url)
htmlpars(url)

