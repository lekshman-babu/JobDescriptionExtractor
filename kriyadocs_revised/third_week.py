import sqlite
f=open("demo2.txt",'r')
indi_skill=""
job=""
skill_dictionary={}

skill=["machine learning","communication","python","html","accounting","sql"]
#creating a new dictionary of skills
for i in skill:
    skill_dictionary[i]=None

if __name__=="__main__":

    print("checking whether the database is available:")
    try:
        storedjob=sqlite.select()
        for i in storedjob:
            print(i)
    except:
        print("table not created \n creating table.....")
        sqlite.create()
        while True:
            eof=f.readline()
            if eof=='':
                break
            eof=eof.replace("\n",'')
            eof=eof.replace(" ",'',1)
            if eof.isupper():
                job=eof.replace(" JOB DESCRIPTION","")
            elif eof.islower():
                indi_skill=eof
                jobskill=[job,indi_skill]
                sqlite.insert(jobskill)
        storedjob=sqlite.select()
        for i in storedjob:
            print(i)
