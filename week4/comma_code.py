# Possible solution to comma code exercise.
# Program contains a function that converts a list into a string using English
# grammer, (without using the join() method).

def list_to_grammer(list_to_convert):
    grammer = ""
    list_length = len(list_to_convert)

    if list_length == 0:
        return ""
    elif list_length == 1:
        try:
            return str(list_to_convert[0])
        except TypeError:
            print("Invalid item in list. Can't convert value to string.")
            return ""
    elif list_length >= 2:
        try:
            for item in list_to_convert[:-2]:
                grammer += "{}, ".format(item)
            grammer += "{} and {}".format(list_to_convert[-2], list_to_convert[-1])
            return grammer
        except TypeError:
            print("Invalid item in list. Can't convert value to string.")
            return ""
        

#######################
## test list_to_grammer function

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(1 + len(spam)):
    seq = spam[:i]
    s = list_to_grammer(seq)
    print(i, seq, repr(s))

print("")
spam = [5, 3.4, True, ['cats', 'bats', 'rats']]

for i in range(1 + len(spam)):
    seq = spam[:i]
    s = list_to_grammer(seq)
    print(i, seq, repr(s))
