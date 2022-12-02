# Python 101 by Anton Ryzhenkov

# Functions as objects

def multiplication(var1,var2):
    return var1 * var2

var3 = 7
var4 = 8

operation = multiplication
print(operation(var3,var4))

# functions can be used as ARGUMENT of other functions

def addition(x,y):
    return x + y

def double(func,x,y):
    return func(func(x,y),func(x,y))

var5 = 7
var6 = 11

print(double(addition,var5,var6))