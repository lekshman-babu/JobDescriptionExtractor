#opening file from second_week.py
f=open("demo2.txt",'r')

a=[]
b=''
skill_dictionary={}

#reading each line the file
while True:
    eof=f.readline()
    if eof=='':
        break
    if eof.isupper():
        if b!='':
            
            #replace first and last word with ''
            b=b.replace(" ",'',1)
            b=b.replace("\n",'')
            skill_dictionary[b]=a
            a=[]
        b=eof
    else:
        if eof.islower():
            
            #replace last word with ''
            eof=eof.replace("\n",'')
            a.append(eof)

#created skill dictionary
print("the dictionary keys are:")
for i in skill_dictionary:
    print(i)

#getting user input
choice=input("choose on for the top: ")
for i in skill_dictionary[choice]:
    print(i)
