# Creating a tuple
my_tuple = (10, 20, 30, 40, 20)

print("Original Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing the tuple
print("Sliced Tuple (index 1 to 3):", my_tuple[1:4])

# Length of the tuple
print("Length of tuple:", len(my_tuple))

# Count of an element
print("Count of 20:", my_tuple.count(20))

# Index of an element
print("Index of 30:", my_tuple.index(30))

# Membership check
print("Is 40 in tuple?", 40 in my_tuple)

# Concatenation of tuples
new_tuple = my_tuple + (50, 60)
print("After concatenation:", new_tuple)

# Converting tuple to list
tuple_to_list = list(my_tuple)
print("Tuple converted to list:", tuple_to_list)
