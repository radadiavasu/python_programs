# Break command
cars = ["ok", "ok", "faulty", "ok", "ok"]

# Using for loop to define break statement
for status in cars:
    if status == "faulty":
        print("Stopping this production line")
        # break
        continue
    print(f"This cars is {status}.")     