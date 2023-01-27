"""Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""
def alphord(str1):
    lst1=[a for a in str1.split("-")]
    lst1.sort()
    print("-".join(lst1))
alphord(input("Enter hyphen separated sequence: "))
        