import config

lottery_numbers = config.lottery_numbers

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

for player in players:
    player_number = player["numbers"]
    player_name = player["name"]
    matched_count = lottery_numbers.intersection(player_number)
    print(f"{player_name} matched {len(matched_count)} numbers and won {100*len(matched_count)} rupees.")
