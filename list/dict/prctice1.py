b = {'name':'adarsh','role':'Developer','domain':'python'}
for keys in b :
    print(keys,':',b[keys])
keys = b.keys()
for i in keys :
    print(b[i])

d = {'a': 1, 'b': 2}
d.clear()
# d is now {}

d = {'a': 1, 'b': 2}
d_copy = d.copy()
# d_copy is {'a': 1, 'b': 2}

keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
# d is {'a': 0, 'b': 0, 'c': 0}

# d is {'a': 0, 'b': 0, 'c': 0}

d = {'a': 1, 'b': 2}
value = d.get('a')  # Returns 1
value = d.get('c', 'default')  # Returns 'default'


d = {'a': 1, 'b': 2}
items = d.items()
# items is dict_items([('a', 1), ('b', 2)])

d = {'a': 1, 'b': 2}
keys = d.keys()
# keys is dict_keys(['a', 'b'])


d = {'a': 1, 'b': 2}
value = d.pop('a')  # Returns 1
value = d.pop('c', 'default')  # Returns 'default'

d = {'a': 1, 'b': 2}
item = d.popitem()  # Returns ('b', 2) or ('a', 1), depending on insertion order

d = {'a': 1}
value = d.setdefault('a', 2)  # Returns 1, as 'a' is already in the dictionary
value = d.setdefault('b', 3)  # Returns 3, and 'b' is added to the dictionary with value 3

d = {'a': 1}
d.update({'b': 2, 'c': 3})
# d is now {'a': 1, 'b': 2, 'c': 3}

d = {'a': 1, 'b': 2}
values = d.values()
# values is dict_values([1, 2])
