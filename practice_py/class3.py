# line=int(input("Enter Line Number: "))

# for i in range(line):
#     for j in range(line):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

line=int(input("Enter Line Number: "))
char=ord("A")

for i in range(line):
    for j in range(line):
        if j <= i:
            print(chr(char), end=" ")
            char+=1
        else:
            print(" ", end=" ")
    print()
