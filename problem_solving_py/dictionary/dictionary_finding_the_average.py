if __name__ == '__main__':
    n = int(input())
    student_marks = {} # an empty dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        size = len(scores)
        student_marks[name] = scores
    query_name = input()
    
    query_scores = student_marks[query_name]
    total_scores = sum(query_scores)
    avg = total_scores/size
    
    # ? Syntax: {[argument_index_or_keyword]:[width][.precision][type]}
    print("{0:.2f}".format(avg))
