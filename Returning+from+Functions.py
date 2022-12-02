# Python 101 by Anton Ryzhenkov

# Returning from functions

def maximum(x,y):
    if x>=y:
       return x
    else:
        return y
    
print(maximum(5,9))
z = maximum(10,3)
print(z)

# code after "return" will never happen

def add_digits(var,var1):
   sum = var + var1
   return sum
   print("Not be printed")

print(add_digits(6,7))