d = {'a': 1, 'b': 2}
d.clear()
d['nm']='rin'
print(d)

keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 1) #assign the values to list items as 1 for all

print(d)


d = {'a': 1, 'b': 2}
value = d.get('a')  # Returns 1
print(value)
value = d.get('c', 'not available')  # Returns 'not available'
print(value)

d = {'a': 1, 'b': 2}
items = d.items()
print(items)
# items is dict_items([('a', 1), ('b', 2)])

d = {'a': 1, 'b': 2}
keys = d.keys()
# keys is dict_keys(['a', 'b'])
print(keys)

d = {'a': 1, 'b': 2}
value = d.pop('a')  # Returns 1
print(value)
value = d.pop('c', 'not available')  # Returns 'default'
print(value)

d = {'a': 1, 'b': 2}
item = d.popitem()  # Returns ('b', 2) or ('a', 1), depending on insertion order
print(item) #Raises KeyError if the dictionary is empty.

d = {'a': 1}
value = d.setdefault('a', 2)  # Returns 1, as 'a' is already in the dictionary
print(value)
value = d.setdefault('b', 3)  # Returns 3, and 'b' is added to the dictionary with value 3
print(value)

d = {'a': 1}
d.update({'b': 2, 'c': 3})
# d is now {'a': 1, 'b': 2, 'c': 3}
print(d)

d = {'a': 1, 'b': 2}
values = d.values()
# values is dict_values([1, 2])
print(values)
