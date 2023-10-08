# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## lenth of the set
print(len(b)) # print the lenth of the set

## Removel of an item
b.remove(5) # Remove 5 from set b 
# b.remove(15) # Throws a error while trying try to remove is not present in set

print(b.pop())
print(b)