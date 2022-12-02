# Python 101 by Anton Ryzhenkov
# Operator Precedence
# List of Python's operator from highest presedence to lowest
'''
**         Exponentiation raise to the power
~+-        Complement, unary plus and minus
*/%//      Multiply, divide, modulo and floor division
+-         Addition and subtraction
>> <<      Right and left bitwise shift
&          Bitwise 'AND'
^|         Bitwise exclusive 'OR' and regular 'OR'
<= < > >=  Comparison operatos
<> == !=   Equality operators
= %= /= //= -= += *= **= Assignment operators
is  is not Identity operators
in  not in Membership operators
not or and Logical operators
'''
print(False == False or True)
print(False == (False or True))
print((False == False) or True)