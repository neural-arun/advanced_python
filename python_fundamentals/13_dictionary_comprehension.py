friends_names = ["Arun","Sarita","Uday","Sunny"]
friends_ages = [22,25,27,17]

friends_info = {
    friends_names[i]:friends_ages[i] 
    for i in range(len(friends_names))

}
print(friends_info)  # This would give a dictionary with name and ages.