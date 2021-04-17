import re

def fun(s):
    return bool(re.match("^([a-z][\w-]+)@([a-z0-9]+)(\.[a-z]{1,3})$", s))
    
    # The given email can be groupped into 3 parts:
    # username + @ + website + . + extension
    # 1.    '^' means start of the expression
    # 2.    () means capture and group
    #       Username can only contain: letters, digits dashes and underscores:
    #       a-z 
    #       \w any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) and additionally '-'
    #       '+' means 1 or more repetitions
    # 3.    Then the '@' should occurs
    #       () means capture and group
    #       Website can only have letters and digits:
    #       a-z and 0-9
    #       '+' means 1 or more repetitions
    # 4.    () means capture and group
    #       Then '.'
    #       a-z
    #       The max length of extension should be 3 so, number of length 1 to 3
    # 5.    '$' means end of the expression
    # https://www.w3schools.com/python/python_regex.asp


def filter_mail(emails):
    return list(filter(fun, emails))

    # filter(function, sequence)
    # Parameters:
    # function: function that tests if each element of a
    # sequence true or not.
    # sequence: sequence which needs to be filtered, it can
    # be sets, lists, tuples, or containers of any iterators.
    # Returns:
    # returns an iterator that is already filtered.


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
