def solution(x, y):
    return list(set(x).symmetric_difference(set(y)))[0]

if __name__ == "__main__":
    x = []
    y = []

    x = [int(i) for i in input().split()]
    y = [int(j) for j in input().split()]

    print(solution(x, y))
