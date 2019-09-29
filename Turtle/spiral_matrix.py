'''
Spiral matrix program
author:Rudrajit
'''

def spiral(m,n,a):#m=rows n=columns a=matrix
    k,l=0,0
    '''
    k=index of starting row
    l=index of starting column
    '''

    while(k<m and l<n):
        
        #printing the first row out of remaining rows
        for i in range(l,n):
            print(a[k][i],end=" ")
        k+=1
        
        #printing the last column out of remaining columns
        for i in range(k,m):
            print(a[i][n-1],end=" ")
        n-=1

        if(k<m):#checking the condition again as k has been increamented
            #printing the last row out of remaining rows
            for i in range(n-1,l-1,-1):#we wanna include l inex as well
                print(a[m-1][i],end=" ")
            m-=1

        if (l<n):#checking the condition again as l has been increamented
            #printing the first column out of remaining columns
            for i in range(m-1,k-1,-1):#we wanna include k index as well
                print(a[i][l],end=" ")
            l+=1

a=[]
count=1
m=int(input("Enter rows:"))
n=int(input("Enter columns:"))
for i in range(m):
    l=[]
    for j in range(n):
        l.append(count)
        count+=1
    a.append(l)
for i in range(m):
    for j in range(n):
        print(a[i][j],end="\t")
    print()
spiral(m,n,a)
    
        
        
        
