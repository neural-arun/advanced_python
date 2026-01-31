try:
    x = int("abc")  # Yha sirf vahi code hota hai jismein error aa sakta hai.
except ValueError:
    print("Invalid number!")  # Agr value error aaye to yha aa jao.

# program does not crashed now.


# Multiple exceptions bhi real world mein common hai.

try:
    x = int(input())
    y = 10 / x
except ValueError:
    print("Number galat hai")
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte")


# else: error na aaaye to kya kare

try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("No error, value is:", x)



# # final structure
# try:
#     risky_code
# except SomeError:
#     handle_error
# else:
#     success_code
# finally:
#     cleanup_code

# Reraising the error.
try:
    x = int("abc")   #👉 Tum error catch karte ho
except ValueError:   
    print("Logging error")   # 👉 Kuch kaam karte ho
    raise    # 👉 Phir wahi error dobara throw kar dete ho

# Final mental code.

# try:
#     risky_code
# except SpecificError as e:
#     handle_or_log
#     raise   # optional
# else:
#     success_code
# finally:
#     cleanup_code