# program that checks if an input name is in a list of names.

names = ["Graham", "John", "Terry", "Eric", "Michael", "Carol"]

print("Enter a name to check:")
check_name = input()

if check_name not in names:
    print("That name is not in the list")
else:
    print("Name found in list")
