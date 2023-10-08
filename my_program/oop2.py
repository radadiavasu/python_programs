movie = ['Major', 'Shershah']

class garage:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<garage {self.cars}>'
    
    def __str__(self):
        return f'<garage with {len(self)} cars.>'
    
ford = garage()
ford.cars.append('Toyota')
ford.cars.append('Focus')

print(ford)    