"""Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run."""
"""x=input("enter a string:")
if x==x[::-1]:
    print("it's a palindrome")
else:
    print("not a palindrome")"""
def palindrome(x):
    if x==x[::-1]:
        print("it's a palindrome")
    else:
        print("not a palindrome")
    
s=input("enter a string:")
palindrome(s)
    