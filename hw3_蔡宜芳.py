# Question No.1
try:
    n = int(input("Please enter a positive integer "))
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        for _ in range(n-i):
            print("*", end="")
        print()
except:
    print("Please provide a valid number")

# Question No.2
try:
    n = int(input("Please enter a positive integer "))
    for i in range(n):
        for _ in range(n-i-1):
            print(" ", end="")
        for _ in range(i+1):
            print("*", end="")
        print()
except:
    print("Please provid a valid number")

# Question No.3
try:
    s1 = input(
        "Please enter two positive integers and seperate with a whitespace ").split()
    s2 = input(
        "Please enter another two positive integers and seperate with a whitespace ").split()
    point1 = list(map(lambda x: int(x), s1))
    point2 = list(map(lambda x: int(x), s2))

    def get_distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(1/2)

    print(get_distance(point1, point2))

except:
    print("Please provid valid numbers")

# # Question No.4
import random
try:
    row = int(input("Please enter the row number "))
    col = int(input("Please enter the column number "))
    matrix = []
    for i in range(row):
        lst = [random.randint(1, 20) for _ in range(col)]
        matrix.append(lst)
    print(matrix)

except:
    print("Please provide valid numbers")
