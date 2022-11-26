import requests
import bs4

#open a file
f=open("demo.txt",'w+')

#request to get the website
res=requests.get("https://www.betterteam.com/job-description")
bs=bs4.BeautifulSoup(res.text,"html.parser")

#create a list with class name 
base=bs.select('.col-md-6.item')
i=0

#only for 5 jobs as of now but can extend
while i!=5:
    #initialize each element of list to ul
    ul=base[i]
    print("----------------------------------------------------------------")

    #get only the link from each href
    link=ul.select('a')[0]['href']
    print(link)

    #next linked page 
    req=requests.get(link)
    bea=bs4.BeautifulSoup(req.text,"html.parser")

    #get the name of the job and store it in upper case
    head=bea.select('.card-title')[0]
    f.write(head.text.upper()+"."+"\n")

    #the 3rd ul in the page has the job requierments
    li=bea.select('ul')[3]

    #get each requierments and store it in a file
    for item in li:
        f.write(item.text.lower()+"\n")
    f.write("\n")
    i+=1
f.close()
