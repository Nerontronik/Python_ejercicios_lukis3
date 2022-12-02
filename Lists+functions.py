# Python 101 by Anton Ryzhenkov

# Lists Functions

# append method
digits = [9,10,11]
print(digits)
digits.append(12)
print(digits)

# len function
digits1= [4,5,6,7,8]
print(len(digits1))

# insert

word = ["Python", "Super!"]
var = 1
word.insert(var,"is")
print(word)

symbols = ["q","w","e","r","t","y"]
print(symbols.index("r"))
print(symbols.index("q"))
'''print(symbols.index("a"))'''

'''max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list'''