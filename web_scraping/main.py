import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.domain.com.au/sale/melbourne-vic-3000/")
if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

# print(response.text)

# soup = BeautifulSoup(response.text,"html.parser")
# print(soup.title.string)


# for i in soup.find_all("a"):
#     print(i.get("href"))
