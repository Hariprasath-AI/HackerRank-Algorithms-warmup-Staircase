# Read this >>>
# assign the single space to the variable
# for loop goes n + 1 no.of times, 1 is the initial value and it is reduced with 'n', value stored in space_limit.
# This means that how many spaces We have to allot infront of the letter '#'. eg: n = 6, at the start of for loop i = 1, space_limit = 6-1 = 5.
# The value 5 is multiplied with the string 'space' and 5 spaces will be stored in variable 'solution'
# Next, i multiplied with hash. This means that how many hash to print in the line stored in the variable hash_limit.
# Just add those two variable and print. We will get right aligned staicase shaped output.  

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
