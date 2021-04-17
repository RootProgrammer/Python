def plusMinus(arr):
    positive = negative = zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    positive_ratio = positive/len(arr)
    negative_ratio = negative/len(arr)
    zero_ratio = zero/len(arr)

    # ? Syntax: {[argument_index_or_keyword]:[width][.precision][type]}.format(argument_value_or_keyword)
    return "{0:.6f}".format(positive_ratio), "{0:.6f}".format(negative_ratio), "{0:.6f}".format(zero_ratio)


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    result = list(plusMinus(arr))

    print("\n".join(map(str, result)))
