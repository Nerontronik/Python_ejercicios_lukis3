# Python 101 by Anton Ryzhenkov

# Opertions with lists

digits = [9,9,9,9,9]
print(digits)
digits[2] = 3
print(digits)
# addition and multiplication in lists
digits1 = [5,6,7]
print(digits1)
print(digits1 + [8,9,10])
print(digits1 * 4)

'''check element in list (in, not)'''
something_words = ["Python", "programm", "good", "forever"]
print("Python" in something_words)
print("Sky" in something_words)
print("forever" in something_words)

digits2 = [3,4,5]
print(not 1 in digits2)
print(1 not in digits2)
print(4 not in digits2)
print(not 4 in digits2)