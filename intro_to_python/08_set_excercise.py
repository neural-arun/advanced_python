"""
We have provided you with two variables:

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set() # This is an empty set, like {}
In this exercise, ask the user for the name of a friend. Add this name to the user_friends set provided.

Finally, print out a set that contains only the name of the friend if the friend is in the 
nearby_people set.

You'll want to calculate the intersection between two sets, and print the result out.

"""


nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()

new_user_friends = input("Enter name of your friend: ")

user_friends.add(new_user_friends)

common_frieds = nearby_people.intersection(user_friends)

print(common_frieds)