import third_week as tw

#iterating through the dictionary and the list
for i in tw.skill_dictionary:
    count=0
    for j in tw.jobskill:
        for k in j[1]:
            if i in k:
                count+=1
    tw.skill_dictionary[i]=count
    
#displaying the new ranked list
rankno=1
print("the ranked skill list")
for i in sorted(tw.skill_dictionary,key=tw.skill_dictionary.get,reverse=True):
    print(f"{rankno} {i} : {tw.skill_dictionary[i]}")


