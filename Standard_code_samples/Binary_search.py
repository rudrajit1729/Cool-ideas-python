#binary search

def binsearch(a,l,r,s):
    
    while (l<=r):
        mid=(l+r)//2
        if(s<a[mid]):
            r=mid-1
        elif(s>a[mid]):
            l=mid+1
        else:
            print("Found at "+str(mid+1))
            return 0
    print("Not found")
    return -1
    
        





a=[x for x in range(1,11)]
s=int(input("\nEnter your number:"))
n=len(a)
x=binsearch(a,0,n-1,s)
