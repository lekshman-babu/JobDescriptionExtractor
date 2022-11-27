f=open("demo2.txt",'r')
a=[]
b=''
skill_dictionary={}
while True:
    eof=f.readline()
    if eof=='':
        break
    if eof.isupper():
        if b!='':
            b=b.replace(" ",'',1)
            b=b.replace("\n",'')
            skill_dictionary[b]=a
            a=[]
        b=eof
    else:
        if eof.islower():
            eof=eof.replace("\n",'')
            a.append(eof)
print("the dictionary keys are:")
for i in skill_dictionary:
    print(i)
choice=input("choose on for the top: ")
for i in skill_dictionary[choice]:
    print(i)