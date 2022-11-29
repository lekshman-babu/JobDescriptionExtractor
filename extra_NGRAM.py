def ngram(string,n):
    a=string.split()
    for i in range(len(a)):
        for j in range(i,i+n):
            print(a[j],end=' ')
        if i+n>len(a)-1:
            break
        print()
ngram("hi i am xyz my friends are yzx ",4)
