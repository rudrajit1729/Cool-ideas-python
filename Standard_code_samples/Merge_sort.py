#merge sort

def split(ar,l,r):
    if l<r:
        mid=(l+r)//2
        split(ar,l,mid)
        split(ar,mid+1,r)
        merge(ar,l,mid,r)

def merge(ar,l,mid,r):
    i=l
    j=mid+1
    k=0
    t=[]
    while i<=mid and j<=r:
        if ar[i]<ar[j]:
            t.append(ar[i])
            i+=1
        else:
            t.append (ar[j])
            j+=1
    for x in range(i,mid+1):
        t.append(ar[x])
    for x in range(j,r+1):
        t.append(ar[x])
    for i in range(l,r+1):
        ar[i]=t[k]
        k+=1
ar=[5,4,3,2,1]
split(ar,0,4)
print(ar)
        
            
