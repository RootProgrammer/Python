if __name__ == '__main__':
    n = int(input())

    l = []

    for i in range(n):
        l.append(i+1)

    print(''.join(str(i) for i in l))
