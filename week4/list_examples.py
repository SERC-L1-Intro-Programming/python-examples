# list examples
#
# Lists contain a series of values in an ordered sequence. Values can be other 
# content types. Lists are contained in square brackets [].

# simple list
spam = ["cat", "bat", "rat", "elephant"]


# index positions
# Individual values in a list can be referenced using the items index position.
# Index positions start at 0. The first item in a list has index position 0, the
# second item has index position 1, and so on.
print(spam[0])  # prints the first item in the list spam


# list in list
# As well as int, float, str, bool, lists can alos contain other lists.
can = [["cat", "bat"],[10,30,50,70]]

print(can[0])       # prints ['cat', 'bat']
print(can[0][1])    # prints bat
print(can[1][3])    # prints 70


# negative indexes
# Negative indexes can be used to reference items from the end of a list. The 
# last item in a list has index position -1, and so on.
spam = ["cat", "bat", "rat", "elephant"]

print(spam[-1])     # prints the last item in spam - 'elephant'
print(spam[-3])     # prints the 3rd item from the end of spam - 'bat'
print("The " + spam[-1] + " is afraid of the " + spam[-3] + ".")


# list slices
# Lists can be scliced so that only a portion of a list is used. Slices contain 
# two index positions seperated by a :
spam = ["cat", "bat", "rat", "elephant"]

print(spam[0:4])    # prints ['cat', 'bat', 'rat', 'elephant']
print(spam[1:3])    # prints ['bat', 'rat']
# if no start value is given, python will use the start of the list.
# if no end value is given, python will use the end of the list. 
print(spam[:-1])    # prints ['cat', 'bat', 'rat']


# list length
# We can find how many items are in a list be using the len() function
spam = ["cat", "bat", "rat", "elephant", "mouse"]
print(len(spam))    # prints 5


# changing values
# Individual values in a list can be changed by using value assignment with an 
# index position
spam = ["cat", "bat", "rat", "elephant", "mouse"]
spam[1] = "dog"
print(spam)         # prints ['cat', 'dog', 'rat', 'elephant', 'mouse']

spam[2] = spam[1]
print(spam)         # prints ['cat', 'dog', 'dog', 'elephant', 'mouse']

spam[-1] = 12345
print(spam)         # prints ['cat', 'dog', 'dog', 'elephant', 12345]



# removing values, with del and remove
# Items can be removed from a list.
# del keyword is used to remove a value at a known index postion
spam = ["cat", "bat", "rat", "elephant", "mouse"]
print(len(spam))
del spam[2]
print(len(spam))
print(spam)

# remove() method is used to remove a specific value without knowning its index 
# postion
spam = ["cat", "bat", "rat"]
spam.remove("bat")
print(spam)         # prints ['cat', 'rat']


# adding items to a list, with append and insert
# append() is used to add a value to the end of a list
spam = ["cat", "bat", "rat"]
spam.append("mouse")
print(spam)         # prints ['cat', 'bat', 'rat', 'mouse']

# insert() is used to insert a value into the list at a given position.
# insert() takes two arguments, the first argument is the index position to 
# insert the value at, and the second argument is the value to insert.
spam = ["cat", "bat", "rat"]
spam.insert(1, "elephant")
print(spam)         # prints ['cat', 'elephant', 'bat', 'rat']


# finding the index position of a value
# The index position of a value can be found using the index() method.
spam = ["cat", "bat", "rat"]
index_pos = spam.index("bat")
print(index_pos)


# list concatenation
# Lists can be joined together using the concatenation operator, +, in a similar
# way that strings can be joined togther.
list1 = [1,2]
list2 = [3,4,5]
print(list1+list2)  # prints [1, 2, 3, 4, 5]


# string magic
# Strings can be indexed the same way that lists are indexed. Each character in 
# a string represents a value in a list.
sentence = "The quick brown fox jumps over the lazy dog."

print(sentence[4])      # prints q
print(sentence[0:8])    # prints The quic

print(sentence[:-4] + "elephant.")  # prints The quick brown fox jumps over the lazy elephant.


# list conditions, in and not in operators
# We can check if a value is in a list using the in operator. If the value is in 
# the list, this will retrun a True value. If the value is not in the list, 
# False will be returned. not can be used with in to reverse the boolean values.
spam = ["cat", "bat", "rat"]

print("cat" in spam)        # prints True
print("mouse" in spam)      # prints False
print("mouse" not in spam)  # prints True


# random
# The random module has methods that can be used with lists.
import random
spam = ["cat", "bat", "rat", "elephant"]
# random.choice() will randomly chose a value from a list
print(random.choice(spam))

# random.shuffle() will randomly reorder a list
random.shuffle(spam)
print(spam)



# spam.reverse()