import requests
f=open("wordlist.txt","r")
for i in f:
    i=i.strip()
    r=requests.get("https://www.google.com/"+i)
    if r.status_code==200:
        print(i)