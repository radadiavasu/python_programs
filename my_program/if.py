friends = ["Jay", "Vasu", "Kunj"]
family = ["Bhavesh", "Vilas", "Labhu-ba(GM)"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello friend")
elif user_name in family: # this elif function work in both else & if 
    print("Hello family")
else:
    print("I don't know you!")        