if __name__ == "__main__":
    #? string.split(separator, maxsplit)
    x, y = [set(input().split())for _ in range(4)][1::2]
    print(len(x-y))
