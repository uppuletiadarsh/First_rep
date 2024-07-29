# Creating a set
my_set = {1, 2, 3}
print("Initial Set:", my_set)

# Adding Elements
my_set.add(4)
print("After adding 4:", my_set)

my_set.update([5, 6, 7])
print("After updating with [5, 6, 7]:", my_set)

# Removing Elements
my_set.remove(3)
print("After removing 3:", my_set)

my_set.discard(2)
print("After discarding 2:", my_set)

popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping one element:", my_set)

my_set.clear()
print("Cleared Set:", my_set)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of set1 - set2:", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# In-place Set Operations
set1.update(set2)
print("After updating set1 with set2:", set1)

set1.intersection_update(set2)
print("After intersecting set1 with set2:", set1)

set1.difference_update(set2)
print("After differencing set1 with set2:", set1)

set1.symmetric_difference_update(set2)
print("After symmetric differencing set1 with set2:", set1)

# Subset and Superset Checking
subset_check = {1, 2}.issubset(set1)
print("{1, 2} is subset of set1:", subset_check)

superset_check = set1.issuperset({1, 2})
print("set1 is superset of {1, 2}:", superset_check)

# Copying
copied_set = set1.copy()
print("Copied Set:", copied_set)
