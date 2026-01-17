# def count_from_zero_to_n(n):
#     for x in range(0, n+1):
#         if n < 0 :
#             raise ValueError("'n' needs to a positive number.")
#         print(x)

# count_from_zero_to_n(-4)


# Ye galat hai kyounki input validation pahle phir logic baad mein.
# loops sirf kaam karta hai rules check nahi karta hai.


def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError("'n' needs to be a positive number.")

    for x in range(0, n + 1):
        print(x)

count_from_zero_to_n(-4)