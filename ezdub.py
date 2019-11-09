import requests
from bs4 import BeautifulSoup

def linkScan(result, var):
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    links = soup.find_all('a',{"class":"s-item__link"})
    #lowercase = links.lower()

    for link in links:
        if var in link.text:
            print(link.attrs['href'])
            print()

var = input("What are you purchasing? (Case Sensitive) ")

print("Searching for '" + var + "'...")

print("Links from EBay:")
print (linkScan(requests.get("https://www.ebay.com/sch/i.html?_nkw=" + var), var))

print("Links from Amazon:")
print(linkScan(requests.get("https://www.amazon.com/s?k=" + var), var))

print("Links from AliExpress:")
print(linkScan(requests.get("https://m.aliexpress.com/wholesale/" + var + ".html?channel=direct&keywords=" + var), var))



print("Links from Staples:")
print(linkScan(requests.get("https://www.staples.com/" + var + "/directory_" + var), var))

#print(result.status_code)


