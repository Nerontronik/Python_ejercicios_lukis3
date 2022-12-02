# Ptyhon 101 by Anton Ryzhenkov

# Exceptions in Python

number1 = 9
number2 = 0
# print(number1/number2)

''' ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.'''

# try/except statement
try:
    number1 = 9
    number2 = 0
    print(number1/number2)
    print("Calculation end")
except ZeroDivisionError:
    print("Error occured")
    print("zero division")
    print("-")

    
try:
    var = 12
except(ValueError, TypeError):    
    print(var + "Python")
    print(var/2)
    print("-")
except ZeroDivisionError:
    print("Divided by zero")
    print("--")
except(ValueError, TypeError):
    print("This is an Error!")
    print("---")
    
try:
    word = "Universe"
    print(word/0)
    print("----")
except:
    print("Error!")
    print("-----")
    
# Raising Exceptions. Use raise statement

print(7)
# raise ValueError
print(11)

name = "321"
'''raise NameError("Bad name!")'''

try:
    number22 = 7/0
except:
    print("Error!!!")
    #raise
    