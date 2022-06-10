from base64 import decode, encode
from encodings import utf_8
import this
from matplotlib.pyplot import text
import requests 
from bs4 import BeautifulSoup
import re
from collections import defaultdict
from values import thisdict,nodata,arr,country,alias2 

cnt=len(thisdict)+len(nodata)

def read():
    path="C:/Users/ayush/Desktop/programming/webscrape/cities.txt"
    with open(path,'r',encoding="utf-8") as y:
        list=y.readlines()[298:]
        loop=149
        for l in list:
            l=l.rstrip()
            x=re.search("\d", l)

            if x: 
                continue

            else:
                loop=loop+1
                print(loop)
                print(l)
                if(loop%50==0):
                    print("-----------------------------------")
                    print("All values")
                    print(thisdict)
                    print("country count")
                    print(country)
                    print("wrong name")
                    print(alias2)
                    print("duplicate cities")
                    print(arr)
                    print("no data found")
                    print(nodata)

                if(l in thisdict):
                    arr.append(l)
                else:
                    create_list(l)
                
    y.close()

def is_true(q,w):
    if(q.upper()!=w.upper()):
        return 1
    return 0
    

def create_list(x):
    url=f'https://en.wikipedia.org/wiki/{x}'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')

    p=soup.find("h1")

    a=soup.find_all("th",class_="infobox-label")
    done=0
    for z in a:
        if(z.text=="Country"):
            hello=z.next_sibling.text
            if re.search("^\xa0", hello):
                print("true")
                hello=hello[1:]

            p2=p.text
            if(p2.upper()!=x.upper()):
                alias2.append(x)
            
                


            thisdict[x]=hello
            
            if hello in country:
                country[hello]+=1
            else:
                country[hello]=1

            done=1
            break
    
    if(done==0):
        nodata.append(x)

          
# read()

print("For read and write, press 1")
print("For fixing no data values, press 2")
print("For sorting countries by number of cites, press 3")
print("For ")

print("-----------------------------------")
print("All values")
print(country)
print("wrong name")
print(alias2)
print("duplicate cities")
print(arr)
print("no data found")
print(nodata)
print(len(thisdict)+len(nodata))







