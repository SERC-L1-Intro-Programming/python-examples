# program that prints out the Collatz sequence from a starting number.
#
# Collatz Sequence
#  - if the number is even, divide by 2.
#  - if number is odd, multiple by 3 and add 1
#  - repeat until number is equal to 1

def collatz(number):
    if number % 2 == 0:
        value = number // 2
    elif number % 2 == 1:
        value = number * 3 + 1
    else:
        return None
    
    print(value)
    return value


print("** Collatz Sequence **")
print("Enter a number: ")
while True: # loop until user enters an int
    try:
        number = int(input())
        break
    except ValueError:
        print("That was not an integer!")
        print("Enter an integer number: ")

# generate Collatz sequence
while number != 1:
    number = collatz(number)
