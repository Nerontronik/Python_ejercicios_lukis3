# Python 101 by Anton Ryzhenkov

# Range function

digits = list(range(12))
print(digits)
# before "range" convert object in list
digits1 = list(range(6,14))
print(digits1)

print(range(12) == range(0,12))
print(range(12) == range(1,12))
print(range(12))
print(range(1,12))

# third element in range function MUST BE integer
digits2 = list(range(4,21,3))
print(digits2)
'''digits3 = list(range(4,21,3.14))'''
print(digits3)
               