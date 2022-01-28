import requests

server = "http://psll.club"
url = input("Enter URL to being short: Ex: https://google.com/\n")
print(f'Shorted Link is: {requests.get(f"{server}/create-short-link?link={url}").text}')