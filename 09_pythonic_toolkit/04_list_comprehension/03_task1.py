# convert the following code into list comprehension.
# names = []
# for n in ["arun", "rohan", "aakash"]:
#     if len(n) > 4:
#         names.append(n.upper())
# print(names)
names = [name.title() for name in ["arun","rohan","aakash"]  if len(name) > 4]

print(names)