cars = [
    {"make": "Toyota", "model": "fiesta", "milage": 45000, "fuel_consumed": 345},
    {"make": "Toyota", "model": "focus", "milage": 95000, "fuel_consumed": 657},
    {"make": "Toyota", "model": "copper", "milage": 78000, "fuel_consumed": 904},
    {"make": "Toyota", "model": "MX-5", "milage": 78000, "fuel_consumed": 256}
]

def calculate_mpg(car):
    mpg = car["milage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} milles per gallon")

# for car in cars:
    calculate_mpg(car)