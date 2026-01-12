class Club:
    def __init__(self, name):
        # __init__ runs when we create a new Club object
        # 'self' refers to the object being created (e.g., my_club)
        self.name = name          # store the club name (e.g., "Arsenal")
        self.players = []         # list to store player names

    def __len__(self):
        # This method runs when len(my_club) is called
        # We return how many players are in the club
        return len(self.players)

    def __getitem__(self, i):
        # This method runs when my_club[i] is used
        # It allows the Club object to behave like a list
        # We return the i-th player from the players list
        return self.players[i]

    def __str__(self):
        # This method runs when print(my_club) is used
        # It returns a user-friendly message
        return f"{self.name} club has {len(self.players)} players."

    def __repr__(self):
        # This method runs when the object is inspected or debugged
        # It shows the internal state of the object
        # This is useful for developers
        return f"Club {self.name}: {self.players}"


# Create a Club object
my_club = Club("Arsenal")

# Add players to the club
my_club.players.append("Rolf")
my_club.players.append("Anne")

# Print number of players (normal list behavior)
print(len(my_club.players))

# Print the club (uses __str__)
print(my_club)

# Developer-style representation (uses __repr__)
print(repr(my_club))

# Access players using indexing (uses __getitem__)
print(my_club[0])
print(my_club[1])
