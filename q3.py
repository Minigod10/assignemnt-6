"""Write a Python function that prints out the first n rows of Pascal's triangle. Note:
Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle:"""
"""rows=int(input("Enter the number of row: "))
list1=[]
for r in range(rows):
    print(' '*(rows-r), end='')
    print(' '.join(map(str, str(11**r))))"""
from math import factorial
def pascal_triangle(x):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
    
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

        print("\n")
n=int(input("Enter the number of row:"))
pascal_triangle(n)
