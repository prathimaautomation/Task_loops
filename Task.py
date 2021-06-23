# Loops and lists

# Tasks

# make a loop with a range that says hello 10 times
for _ in range(10):
    print("hello")
# create another loop with a range that asks for names and appends to list names
list_names = []
for _ in range(5):
    list_names.append(input("enter a name: "))
#  make a loop that iterated over each name in list_name and format's it into lowercase in a new variable called list_names_lower
list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())

#  Iterate over the list of values to find if they are even
list_of_values = [1, 23, 42, 22, 53, 56, 4, 9, 8]
for val in list_of_values:
    if val % 2 == 0:
        print(f'{val} is even')
## Acceptance Criteria

#  all tasks have been done.
