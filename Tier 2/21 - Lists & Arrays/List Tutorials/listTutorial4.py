"""

Tutorial 4: Sorting and Reversing Lists
Sorting lists using the sorted() function and the .sort() method.
Custom sorting using the key parameter.
Reversing a list using the reversed() function or the .reverse() method.
Sorting lists in place versus creating a new sorted list.

"""

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Sorting lists
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 5, 6, 8, 9, 10]

# Reversing lists
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [6, 5, 9, 8, 10, 1]
