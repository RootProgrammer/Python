def find_goodness_score(string):
    size = len(string)
    score_limit = size//2
    score = 0

    for i in range(score_limit):
        j = i+1
        if string[i] != string[size-j]:
            score += 1

    return score


test_cases = int(input())

for i in range(1, test_cases+1):
    length, target_score = [int(j) for j in input().split()]
    string = input()

    minimum_operation = abs(target_score - find_goodness_score(string))

    print(f"Case #{i}: {minimum_operation}")
