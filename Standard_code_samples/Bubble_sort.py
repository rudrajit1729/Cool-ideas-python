def bubble(l):
    n=len(l)
    for i in range (n):
        for j in range (n-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
a=[5,4,3,2,1]
print(bubble(a))
