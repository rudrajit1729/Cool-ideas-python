def checknum(num):
    iterations=1
    while(num!=1):
        if num%2==0:
            num=num//2
        else:
            num=3*num+1
        iterations+=1
    print(num,iterations)

for i in range(20,31):
    checknum(i)
/*
when n is even set n as n/2.else set n as 3n+1.
Repeat process till num becomes 1.
Here analyse that smaller number doesnt imply algo will take lesser steps or
vice versa.
Still unsolved problem in computer science.
Go and find more on google.
*/
