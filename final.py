import tkinter
from tkinter import *
import requests
from bs4 import BeautifulSoup
keyterms = ["s-item__link","standard-type__product_title"]
x=0
var=""
printable=""
staplesstring = "https://www.staples.com"
root=Tk()
def linkScan(result, var):
    soup = BeautifulSoup(result.content, 'lxml')

    links = soup.find_all('a',{"class":keyterms[x]})
    #lowercase = links.lower()

    for link in links:
        if var in link.text:
            if x == 0:
                toShow=Label(root, link.attrs['href'])
            if x == 1:
                toShow=Label(root,staplesstring+attrs['href'])

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    waiting = Label(root,text="Searching... This might take a while...")
    waiting.pack()
    notifyeb=Label(root,text="EBay:")
    notifyeb.pack()
    linkScan(requests.get("https://www.ebay.com/sch/i.html?_nkw=" + var), var)
    notifyst=Label(root,text="Staples")
    notifyst.pack()
    x=1
    linkScan(requests.get("https://www.staples.com/" + var + "/directory_" + var), var)

prompt = Label(root,text="Enter the electronic product you need (Case Sensitive)")
prompt.pack()
textBox=Text(root, height=2, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Search", 
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()

