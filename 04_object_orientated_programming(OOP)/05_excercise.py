class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)
    
    def __getitem__(self,i):
        return self.players[i]
    
    
    def __str__(self):
        return f"{self.name} club has {len(self.players)} players."
    
    def __repr__(self):
        return f"Club {self.name}: {self.players}"



my_club = Club('Arsenal')


my_club.players.append("Rolf")
my_club.players.append("Anne")


print(len(my_club.players))
print(my_club)