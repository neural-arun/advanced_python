import config

lottery_numbers = config.lottery_numbers

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# 1. Initialize variables to keep track of the winner
top_player_name = ''
top_player_winnings = 0

for player in players:
    player_number = player["numbers"]
    player_name = player["name"]
    
    # Calculate matches
    matched_numbers = lottery_numbers.intersection(player_number)
    count = len(matched_numbers)
    
    # Calculate winnings (Power, not multiply)
    winnings = 100 ** count
    
    # 2. Compare: Is this player better than the current top player?
    if winnings > top_player_winnings:
        top_player_winnings = winnings
        top_player_name = player_name

# 3. Print the final winner after checking everyone
print(f"{top_player_name} won {top_player_winnings}.")