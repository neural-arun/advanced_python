evens = []
for i in range(21):
    if i % 2 == 0:
        evens.append(i)

print(evens)

# that was normal loop now it is turn of list comprehension.

even_list = [even for even in range(21) if even % 2 == 0]
print(even_list)