# Example 3: Nested loops to iterate over a dictionary of lists
data = {'fruits': ['apple', 'banana', 'cherry'],'colors': ['red', 'yellow', 'purple']}

# Iterate over each key-value pair in the dictionary
for key, value_list in data.items():
    print("The key :",key)
    # Iterate over each element in the list associated with the key
    for item in value_list:
        print("-----",item)
    print()

# Output:
# fruits:
# - apple
# - banana
# - cherry
# 
# colors:
# - red
# - yellow
# - purple
