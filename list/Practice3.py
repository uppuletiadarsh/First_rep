my_list = [1, 2, 3]

# Append an element
my_list.append(4)  # my_list is now [1, 2, 3, 4]

# Insert an element
my_list.insert(2, 5)  # my_list is now [1, 2, 5, 3, 4]

# Remove an element by value
my_list.remove(2)  # my_list is now [1, 5, 3, 4]

# Remove an element by index
popped_item = my_list.pop(1)  # my_list is now [1, 3, 4], popped_item is 5

# Reverse the list
my_list.reverse()  # my_list is now [4, 3, 1]

# Sort the list
my_list.sort()  # my_list is now [1, 3, 4]

print(my_list)  # Output: [1, 3, 4]
