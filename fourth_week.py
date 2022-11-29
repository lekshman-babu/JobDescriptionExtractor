import third_week as tw
for i in tw.skill_dictionary:
    count=0
    for j in tw.jobskill:
        for k in j[1]:
            if i in k:
                count+=1
    tw.skill_dictionary[i]=count
print("the ranked skill list")
for i in sorted(tw.skill_dictionary,key=tw.skill_dictionary.get,reverse=True):
    print(f"{i} : {tw.skill_dictionary[i]}")


