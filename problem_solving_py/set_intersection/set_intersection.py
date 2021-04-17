if __name__ == "__main__":
    x, y = [set(input().split()) for _ in range(4)][1::2]
    print(len(x & y))
