import json
# We can use "with" function to open & close. we dont need to write manually oepn & close.
with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file) # read file & turns into a dictonary

# file.close() # we don't need to write this function because we already defined "as file" means it can automatically close.

file = open('friends_json.txt', 'r')
file_contents = json.load(file) # read file & turns into a dictonary

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Tata', 'model': 'Range Rover'},
    {'make': 'Mahindra', 'model': 'Thar'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Ferrari", "released": "2005"}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])