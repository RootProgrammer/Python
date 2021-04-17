if __name__ == "__main__":
    _, x = input(), set(input().split())
    # _ is a variable to store or discard unnecessary inputs.
    _, y = input(), set(input().split())
    print(len(x ^ y))
