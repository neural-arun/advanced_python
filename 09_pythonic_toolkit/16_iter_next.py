lst = [1,2,3]
# for x in lst:
#     print(x)

# ab python mein internally kya ho raha hai.

it = lst.__iter__()
while True:
    try:
        x = it.__next__()
        print(x)
    except StopIteration:
        break

# ye hai for x in lst:
        #    print(x)
