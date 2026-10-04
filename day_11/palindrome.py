"""
A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

"""

string = "A man, a plan, a canal: Panama"

palindrome = ""

for word in string:

    if word.isalnum():

        palindrome += word.lower()

if palindrome == palindrome[::-1]:

    print(True)

else: print(False)

