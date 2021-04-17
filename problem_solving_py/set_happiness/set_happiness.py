if __name__=="__main__":
    # x,y,z=[input().split()for _ in range(4)][1:] >>> this type of input have time complexity
    _ = input()
    x = input().split()
    y = set(input().split())
    z = set(input().split())
    print(sum((i in y)-(i in z)for i in x))