print("\t\t\t+---------------+\n\t\t\t|Number Patterns|\n\t\t\t+---------------+\n")

r=int(input("Enter number of rows: "))

print("\n1. Number Pattern in Right Triangle(forward columning):\n")

for row in range(r):
    for column in range(row+1):
        print(column+1, end=" ")

    print()

print("\n2. Number Pattern in Right Triangle(reverse columning):\n")

for row in range(r):
    for column in range(row,-1,-1):
        print(column+1, end=" ")

    print()


print("\n3. Number Pattern in Right Triangle(ascending row number):\n")

for row in range(r):
    for column in range(row+1):
        print(row+1, end=" ")

    print()

print("\n4. Number Pattern in Right Triangle(descending row number):\n")

for row in range(r):
    for column in range(row+1):
        print(r-row, end=" ")

    print()
