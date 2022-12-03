import third_week as tw
import sqlite as sq



storedjob=sq.select()

for i in tw.skill_dictionary:
    count=0
    for j in storedjob:
        l,m=j
        if i in m:
            count+=1
    tw.skill_dictionary[i]=count
print("the ranked skill list")
rankno=1
for i in sorted(tw.skill_dictionary,key=tw.skill_dictionary.get,reverse=True):
    print(f"{rankno} {i} : {tw.skill_dictionary[i]}")
    rankno+=1
