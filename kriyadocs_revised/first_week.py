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

joblist=["Machine Learning","Data Scientist","Web Developer","Python Developer"]
#only for 5 jobs
while i!=len(base):
    #initialize each element of list to ul
    ul=base[i]
    #print("----------------------------------------------------------------")

    #get only the link from each href
    link_text=ul.select('a')[0].getText()
    link=""

    for item in joblist:
        if item in link_text:
            link=ul.select('a')[0]['href']


            #next linked page
            req=requests.get(link)
            bea=bs4.BeautifulSoup(req.text,"html.parser")
            #the 3rd ul in the page has the job requierments
            li=bea.select('ul')[3]
            f.write(link_text.upper()+"."+"\n")
    
            #get each requierments and store it in a file
            for item in li:
                f.write(item.text.lower()+"\n")
            f.write("\n")
    i+=1
f.close()