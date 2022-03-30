def Staircase(n):
    space = ' '
    for i in range(1, n+1):
        space_limit =  n - i
        if space_limit > 0:
            solution = space_limit * space
            hash_limit = i * '#'
            print(solution + hash_limit)
        elif space_limit == 0:
            print(i * '#')

if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 100:
        Staircase(n)
    else:
        print("out of Constraint")
