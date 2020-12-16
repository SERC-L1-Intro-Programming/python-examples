# collecting names
# program that collects a series of names

names  = []

while True:
    print("Enter the name of student number " + str(len(names) + 1) + ".")
    print("Enter nothing to stop.")

    new_name = input()

    if new_name == "":
        break
    else:
        names = names + [new_name]  # list concatenation

print("The names of the students are:")
for name in names:
    print(" " + name)
