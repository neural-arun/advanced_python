cars = ["good","good","good","good","good","good","bad","bad","good"]

for car in cars:
    if car == "good":
        print("This car is good. shipping it now.")
        continue
    if car == "bad":
        print("This car have some damage. we are skipping this car.")
        continue


# if we want to stop the shipping on the arrival of a bad car then we will use break instead of continue.