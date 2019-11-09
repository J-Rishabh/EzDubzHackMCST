import requests
from bs4 import BeautifulSoup


keyterms = ["s-item__link","standard-type__product_title"]
x=0
staplesstring = "https://www.staples.com"
def linkScan(result, var):
    soup = BeautifulSoup(result.content, 'lxml')

    links = soup.find('a',{"class":keyterms[x]})
    #lowercase = links.lower()

    if var in links.text:
        if x == 0:
            print(links.attrs['href'])
        elif x == 1:
            print(staplesstring + links.attrs['href'])

        print()


var = input("What are you purchasing? (Case Sensitive) ")


print("Searching for '" + var + "'...")

print("Links from EBay:")
print (linkScan(requests.get("https://www.ebay.com/sch/i.html?_nkw=" + var), var))

x=1
print("Links from Staples:")
print(linkScan(requests.get("https://www.staples.com/" + var + "/directory_" + var), var))

x=2

#print("Links from Amazon:")
#print(linkScan(requests.get("https://www.amazon.com/s?k=" + var), var))

#print("Links from AliExpress:")
#print(linkScan(requests.get("https://m.aliexpress.com/wholesale/" + var + ".html?channel=direct&keywords=" + var), var))





#print(result.status_code)
