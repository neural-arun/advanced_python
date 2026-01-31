class Car:
    # This is a class (blueprint) for Car.
    def __init__(self,make,model):
        # this is a constructor .
        # jab bhi koi car banega ye constructor chalega.
        self.make = make
        self.model = model

    def __repr__(self,): # special function: used when python has to show or print the car.
        return f"Company: {self.make}, Model: {self.model}"
    

class Garage:
    def __init__(self):
        self.cars = [] # Garage ke andar ek cars ke naam ki list bana di.

    def __len__(self):
        return (len(self.cars))
    # Ye bhi ek special function hai.
    # Jab bhi koi len(Garage) call karega to kitne cars hai uske number aa jayega.
    
    def add_car(self,car): # Ye ek normal function hai.
        # Ye Garage mein car add karta hai
        # self --> Garage
        # car --> jo car add karni hai
        if not isinstance(car,Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to the Garage but only 'Car' can be added.")
        self.cars.append(car)


ford = Garage()  # Yha Garage bna diya 
fiesta = Car("ford","fiesta")  # yha car bna di. jise abhi garage mein dalna baaki hai.

try:
    ford.add_car(fiesta)
except TypeError:
    print("Your car was not a car!")
finally:
    print(f"Garage has {len(ford)} cars.")


print(ford.cars)  # printing all the cars in the ford garage.

for car in ford.cars:
    print(car)    # doing the same thing but with for loop.