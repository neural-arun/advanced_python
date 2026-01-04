ages = [22,24,27,17,13]

odd_ages = [age for age in ages if age % 2 != 0]

print(odd_ages)


friends = ["Arun","sarita","uday","sunny"]
guests_arrived = ["Lanka","Pintu","deepak","Arun","sunny","uday"]

friends_lower = [friend.lower() for friend in friends]

present_friends = [guest.lower() for guest in guests_arrived if guest.lower() in friends_lower]

print(present_friends)