age = 20

is_adult = age >= 18    # This is True. this is exactly similar to is_adult = True
print(is_adult)
is_adult = age <18     # this is False, this is exactly similar to is_adult = False
print(is_adult)
is_twenty = age == 20  # this is exactly similar to is_twenty = True

print(is_twenty)

# Practice question

age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job)

# This results True because of higher priority keyword
# "and" have higher priority than "or".