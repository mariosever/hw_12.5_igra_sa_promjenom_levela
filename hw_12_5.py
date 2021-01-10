# Use functions to make the game more modular.

# Also try to add another while loop so the user can play many rounds of the game without having to re-run the program each time.

# Optional task: game levels - You can let user choose the level of the game


import json
from hw_12_5_functions import play_game
from hw_12_5_functions import get_top_scores

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        play_game(level=level)
    elif selection.upper() == "B":
        if len(score_list) == 0:
            print("The score list is empty at the moment, please play to fill it in.")
        else:
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break





