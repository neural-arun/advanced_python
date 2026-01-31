family = ["Arun","Sarita","Uday","Sunny","Ayush"]

for counter,member in enumerate(family):
    print(counter,member)

for counter,member in enumerate(family, start=1):  #This starts counter from 1.
    print(counter,member)