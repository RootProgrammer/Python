cube = lambda x: x**3

def fibonacci(n):
    fib = [0,1]
    [fib.append(sum(fib[-2:])) for f in range(2,n)]
    return fib[:n]

if __name__ == '__main__':
    n = int(input())
    
    # print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))
