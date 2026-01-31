for num in range(0,6):
    print(num)
else:
    print("all the numbers are printed successfully.")

# if we put a break keyword in between the else will not be executed.

for num1 in range(0,10):
    print(num1)
    if num1 == 4:
        break
else:
    (print("All the numbers were printed."))  
# Now this will not be executed because of break keyword execution in the middle.