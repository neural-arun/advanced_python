ages = {"arun":22,"sarita":24,"uday":27}

print(ages["arun"])

ages["ashwani"] = 17  # This adds new key value pairs.

print(ages)


# Using list as a tuple/list of dictionaries.

my_siblings_ages = [
    {"arun":22},
    {"sarita":24},
    {"uday":27}
]

print(my_siblings_ages[0]["arun"])  # This would result in 22.


