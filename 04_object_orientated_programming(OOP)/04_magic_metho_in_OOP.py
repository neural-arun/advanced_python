class Garage:
    def __init__(self):
        self.car = []
        
    def __len__(self):
        return len(self.car)
    
    def __getitem__(self,i):
        return self.car[i]
    
    def __repr__(self):
        return f"Garage with {len(self.car)} cars."
    
    def __str__(self):
        return f"This garage have {len(self.car)} car."
    
ford = Garage()
ford.car.append("Bolero")
ford.car.append("fiesta")
ford.car.append("wagnor")

print(ford[1])

for cars in ford:
    print(cars)

print(ford)