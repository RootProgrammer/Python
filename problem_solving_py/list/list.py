if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd = input().split()
        fn = cmd[0]
        args = cmd[1:]
        if fn != "print":
            fn += "("+",".join(args)+")"
            eval("arr."+fn)
        else:
            print(arr)
