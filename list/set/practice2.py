"""a = set()
print(a)

b = [1,2,3,4,4,5,1,3,]
c = set(b)
print(c)

# adding element

a = set()
a.add(12)
print(a)

# update()
# m -1
a = {1, 2, 3, 4, 5}
b = {"adarsh","Python"}
a.update(b)
print(a)
# m - 2
new= set()
new.update(a,range(20,30),range(200,205))
print(new)

# remove() -- if element not found it raises an exception
new.remove("adarsh")
new.remove("Python")
print(new)

# discard()
new.discard(20)
print(new)

# set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {10,20,30}

# union()
union_set = set1.union(set2,set3) # combines all the sets with unique values which are passed as arguments
print(union_set)


# intersection()
intersection_set = set1.intersection(set2) # return the common element in the list
print(intersection_set)

# difference()
difference_set = set1.difference(set2) # the set 1 compared to set 2 return the values of set 1 not present in the set
print(difference_set)

# symmetric_differenc
symmetric_difference_set = set1.symmetric_difference(set2) # the both sets are compared with each other and returns the values not present in the set 
print(symmetric_difference_set) # elements that are in either of two sets, but not in both at the same time.



set1.intersection_update(set2)
print("After intersecting set1 with set2:", set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}
print(set1)  # Output: {1, 2, 3, 4}



set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.intersection_update(set2)
print(set1)  # Output: {3, 4}

subset_check = {1, 2}.issubset(set1)
print("{1, 2} is subset of set1:", subset_check)

superset_check = set1.issuperset({1, 2,3,4})
print("set1 is superset of {1, 2}:", superset_check)

# issuperset() is a method in Python sets that checks whether all elements of another set are present in the calling set
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print(set1.issuperset(set2))  # Output: True

# issubset() is a method in Python sets that checks whether all elements of one set are present in another set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))  # Output: True

set1 = {1, 8, 3, 4,9,2}
print(set1)
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2) # the set 1 compared to set 2 return the values of set 1 not present in the set
print(difference_set)


symmetric_difference_set = set1.symmetric_difference(set2) # the both sets are compared with each other and returns the values not present in the set 
print(symmetric_difference_set) # elements that are in either of two sets, but not in both at the same time.


# This returns a set containing all elements that are in either set1 or set2, but not in both.
