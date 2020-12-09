# Functions can have multiple parameters, and the parameters can be given default
# values. If an argument is not passed to the function, then the default value is
# used instead.
def greetings(name="Charlie", age=70):
    print("Hello {0:s}. You are {1} years old.".format(name, age))

name="Snoopy"
# position of arguments must be the same as the position of the parameters in the
# function definition.
greetings(name, "still young")

# if the function is called without any arguments, the default values are used instead.
greetings()
