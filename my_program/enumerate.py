friends = ["Vasu", "Kunj", "Jay", "Parth"]

for counter,friend in enumerate(friends):
    print(counter)
    print(friend)
    
print(list(enumerate(friends))) # In list form []
print(dict(enumerate(friends))) # In dict form {}