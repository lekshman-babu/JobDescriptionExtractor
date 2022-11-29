f=open("demo2.txt",'r')
indi_skill=[]
job=[]
skill_dictionary={}
jobskill=[]

skill=["work experience","communication","verbal","degree","typing","certification","programming","analytical","ms office","multitasking"]
#creating a new dictionary of skills
for i in skill:
    skill_dictionary[i]=None

#creating a list of list for all the scanned jobs
while True:
    eof=f.readline()
    if eof=='':
        break
    eof=eof.replace("\n",'')
    eof=eof.replace(" ",'',1)
    if eof.isupper():
        if job!=[]:
            job=[]
        job.append(eof)
    if eof.islower():
        indi_skill.append(eof)
        jobskill.append([job,indi_skill])
        indi_skill=[]

#only displaying jobs when this program is called
if __name__=="__main__":
    print(skill_dictionary)
    print(jobskill)
