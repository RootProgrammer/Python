r=int(input("Enter number of rs (>6): "))
c=r+(r-5)
mid=c//2

print()

for i in range(r):
    for j in range(c):
        if i==2 or i==(r-3) or (i+j)==mid or (j-i)==mid or (i-j)==2 or (i+j)==(c+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()