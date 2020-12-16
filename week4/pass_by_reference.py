# pass by refence example
#
# Some variable types in Python when passed to a function, rather than passing
# the value of the variable, a reference (memory location) is passed instead. If
# that parameter is modified in the function, the value of the variable that was
# passed will also be modified.

def eggs(list_parameter):
    list_parameter.append('bacon')

spam = [1,2,3]
print("Value of spam before being passed: ", spam)
eggs(spam)
# note how spam is being used outside the scope of the function eggs()
print("Value of spam after being passed : ", spam)
