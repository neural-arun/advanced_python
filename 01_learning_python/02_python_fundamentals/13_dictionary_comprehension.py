friends_names = ["Arun","Sarita","Uday","Sunny"]
friends_ages = [22,25,27,17]

friends_info = {
    friends_names[i]:friends_ages[i] 
    for i in range(len(friends_names))

}
print(friends_info)  # This would give a dictionary with name and ages.



guests = [('rolf', 25), ('adam', 28), ('jen', 24)]

guests_as_a_dict = dict(guests)
print(guests_as_a_dict)  # it is the best way to turn the above list into guests.