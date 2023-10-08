from turtle import update


myDict = {
    "Fast": "In a Quick Manner",
    "Vasu": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'vasu': 'player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # prints the keys of the dictionary
print(myDict.values()) # prints the keys of the dictionary
print(myDict.items()) # prints the (keys, value) of all  contents the dictionary
print(myDict)
updateDict = {
    "Parth": "Friend",
    "Vasu": "Dancer"
}
myDict.update(updateDict) # update the dictonary by adding key-value pairs from updateDict
print(myDict)

# the differns between .get and [] syntex in dictionary
print(myDict.get("vasu2")) # returns noneas vasu2 is not present in the dictionary
print(myDict["Vasu2"]) # throws an error as vasu2 is not present in the dictionary