n=int(input("Enter dimension:"))
if n%2==0:
    print("Not possible")
    exit()
def magic_square(n):
    m=[[0 for i in range (n)] for i in range(n)]
    k=0
    r=n-1
    c=n//2
    while(k<n*n):
        k+=1
        m[r][c]=k
        if (m[(r+1)%n][(c+1)%n]==0):
            r=(r+1)%n
            c=(c+1)%n
        else:
            r-=1
    for i in range(n):
        for j in range(n):
            print(m[i][j],end=" ")
        print()
    print("\nSum=",str(n*(n**2+1)/2))#sum of rows=columns=diagonals=n(n^2+1)/2
magic_square(n)
