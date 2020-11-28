# This program says hello and asks the user for their name.

print("Hello")

print("What is your name?")
user_name = input()
print("It is good to meet you " + user_name)
# The len() function works out the length of an object. In this case, it works
# out how many characters are in the string passed to it.
print("The length of your name is " + str(len(user_name)) + "characters long.")

print("What is your age?")
user_age = input()

# option 1 - split up sets into several lines so easier to follow
new_age = int(user_age) + 1                             # cast input to int so we can add 1 to it
print("You will be " + str(new_age) + " next year.")    # cast new_age to string, so we can concatenate with other strings

# option 2 - cast, add 1, cast back on one line
# print("You will be " + str(int(user_age) + 1) + " next year.")
