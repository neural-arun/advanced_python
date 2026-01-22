def count_upto(n):
    for num in range(0,n+1):
        yield num

for i in count_upto(1000000):
    print(i)