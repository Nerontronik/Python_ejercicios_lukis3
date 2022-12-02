# Python 101 by Anton Ryzhenkov

# Operations with Dictionaries

squares = {3:9,4:16,5:25,6:"error",7:49}
print(squares)
squares[8] = 64
squares[6] = 36
print(squares)

numbers = {
    5:"five",
    6:"six",
    7:"seven",
    }
print(5 in numbers)
print("six" in numbers)
print(9 not in numbers)
print(10 in numbers)

# dictionary method "get"

pairs = {2:"orange",
         "banana":[7,8,9],
         True:False,
         None:"True",
         }
print(pairs.get("banana"))
print(pairs.get(10))
print(pairs.get(2345, "not in dictionary"))