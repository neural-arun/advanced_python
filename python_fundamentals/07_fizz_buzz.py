for num in range(0,101):
    
    
    if num % 3 == 0 and num % 5 == 0:
        num = "fizzbuzz"
    elif num % 5 == 0:
        num = "buzz"

    elif num % 3 == 0:
        num = "fizz"
        
    print(num)