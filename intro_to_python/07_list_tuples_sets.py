friends = ['Arun',"Uday","Sarita"]
friends.append("sanny")
friends.remove("Arun")


# tuples 
# Not mutable we can not change the elements of the tuples 
# we have to make a new tuple to change the elements of tuples

#sets

# unordered and mutable

set1 = {"Arun", "Arun", "Uday"}
print(set1)


#advanced set operations

num_set1 = {1,2,3,4}
num_set2 = {4,5,6,7}

difference = num_set1.difference(num_set2)  # this prints out elements which are in num_set 1 but not in 
# num_set2
print(difference)   #{1,2,3}

difference2 = num_set2.difference(num_set1)  # prints which are in 2 but not in one
# output:  {5,6,7}
print(difference2)

symmetric_difference = num_set1.symmetric_difference(num_set2)
print(symmetric_difference)  # print only those which are in only one set not in  both.

intersection = num_set1.intersection(num_set2)
print(intersection)  # prints only the elements which are in both sets.

union = num_set1.union(num_set2)
print(union)

