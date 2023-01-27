"""Write a Python function to check whether a string is a pangram or not. Note: Pangrams
are words or sentences containing every letter of the alphabet at least once. For
example: "The quick brown fox jumps over the lazy dog"""
"""import string
s=input("enter a string:")
alp="abcdefghijklmnopqrstuvwxyz"
flag=0
for i in alp:
    if i not in s.lower():
        flag=1

if flag==1:
    print("not a pangram")
else:
    print("A pangram")"""
def pangrams(x):
    alp="abcdefghijklmnopqrstuvwxyz"
    flag=0
    for i in alp:
        if i not in x.lower():
            flag=1
    if flag==1:
        print("not a pangram")
    else:
        print("A pangram")

s=input("enter a string:")
pangrams(s)
