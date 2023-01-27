"""Write a Python function to check whether a number is perfect or not. According to
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a
number that is half the sum of all of its positive divisors (including itself)."""           
def perfect_number(x):
    y=[]
    for i in range(1,x):
        if x%i==0:
            y.append(i)
    sums=sum(y)
    if sums==x:
        print(x," is a perfect number")
    else:
        print(x," is not a perfect number")
input1=int(input("Enter a number:"))
perfect_number(input1)