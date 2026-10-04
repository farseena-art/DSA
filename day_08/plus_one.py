"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

"""

digits = [1,2,3]

n = len(digits)

for i in range(n-1,-1,-1):

    if digits[i] < 9:

        digits[i] += 1

        print(digits)

        break

    else: digits[i] = 0

else:
    
    print([1] + digits)   