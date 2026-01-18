"""
1- pahle people_nearby.txt se readlines() karo aur un names ko clean karo.
2- unhe ek list mein store karo
3- user se teen naam lo.
4- proper format karke list mein user se liye gaye teen names ko bhi store karo.
5- if user se liye gaye name is in the people_nearby" add them to friends nearby.


"""


from pathlib import Path
BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "people_nearby.txt"

with open(file_path,"r") as f:
    people_names = f.readlines()  # people_names is a list of names in a different format.
    
clean_people_name = []
for name in people_names:
    clean_name = name.strip().title()
    clean_people_name.append(clean_name)

nearby_friends = []
for friends in range(1,4):
    friends = input(f"Enter your friend name: ").strip().title()
    nearby_friends.append(friends)

city_friends = []

for friend in nearby_friends:
    if friend in clean_people_name:
        city_friends.append(friend)

new_file_path = BASE_DIR / "friends_nearby.txt"
with open(new_file_path,"a") as f:
    for close_friend in city_friends:
        f.write(close_friend + "\n")

print("Names added successfully!")
