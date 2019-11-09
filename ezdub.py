import requests
from bs4 import BeautifulSoup


keyterms = ["s-item__link","",""]
keyterms = ["standard-type__product_title","as-links-name more","s-item__link"]
websitestring = ["https://www.staples.com","",""]
x=0

def linkScan(result, var):
    soup = BeautifulSoup(result.content, 'lxml')

    links = soup.find('a',{"class":keyterms[x]})
    #lowercase = links.lower()

    if var in links.text:    
        print(websitestring[x] + links.attrs['href'])
        print()

var = input("What are you purchasing? (Case Sensitive) ")


print("Searching for '" + var + "'...")
print("It may take a while...")

print("Links from Staples:")
print(linkScan(requests.get("https://www.staples.com/" + var + "/directory_" + var), var))

x=1
print("Links from Apple:")
print(linkScan(requests.get("https://www.apple.com/us/search/" + var), var))

x=2
print("Links from EBay:")
print (linkScan(requests.get("https://www.ebay.com/sch/i.html?_nkw=" + var), var))



#print("Links from Best Buy:")
#print(linkScan(requests.get("https://www.bestbuy.com/site/searchpage.jsp?st=" + var), var))
#
#https://www.bestbuy.com




#print("Links from Walmart:")
#print(linkScan(requests.get("https://www.walmart.com/search/?query=" + var), var))
#product-title-link line-clamp line-clamp-2
#https://www.walmart.com

#print("Links from Amazon:")
#print(linkScan(requests.get("https://www.amazon.com/s?k=" + var), var))

#print("Links from AliExpress:")
#print(linkScan(requests.get("https://m.aliexpress.com/wholesale/" + var + ".html?channel=direct&keywords=" + var), var))





#print(result.status_code)


