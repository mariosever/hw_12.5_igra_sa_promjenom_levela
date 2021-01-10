import json
import random
import datetime

def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    change_level = "hard"

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
        else:
            print("Your guess is not correct.")

        # promjena levela
        if attempts == 5 and level == "hard":
            change_level = input("Would you like to change level to easy? Enter yes/no: ")
            if change_level == "yes":
                level = "easy"


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list



