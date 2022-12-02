# Python 101 by Anton Ryzhenkov

# Loops
# While loop

smth_words = ["Python","is","Super","programming language"]
counter = 0
maximum_indx = len(smth_words)-1

while counter <= maximum_indx:
    word = smth_words[counter]
    print(word + "!")
    counter = counter + 1
    
# for loop
something_words = ["Python","Peace","life","forever"]
for word1 in something_words:
    print(word1 + "!")
#for loop is like foreach loop    

for var in range(7):
    print("Super Nova!")