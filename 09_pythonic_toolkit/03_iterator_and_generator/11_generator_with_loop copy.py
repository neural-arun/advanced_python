# def count_upto(n):
#     for num in range(0,n+1):
#         yield num

# for i in count_upto(100):
#     print(i)

nums = (i for i in range(100))
print(type(nums))#<class 'generator'>
