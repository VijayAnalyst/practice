# https://www.higherlowergame.com/ --> online game 

# https://appbrewery.github.io/python-day14-demo/ --> Final Output


from art import logo,vs
#print higher lower game logo from art file
print(logo)

from game_data import data

#generate a random account from the game data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} is a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    #if a_followers > b_followers and guess =='A'
    # if a_followers > b_followers:
    #     if guess == "A":
    #         return True
    #     else:
    #         return False 
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

score = 0
Should_continue = True

account_B = random.choice(data)

while Should_continue:
    
    account_A = account_B
    account_B = random.choice(data)

    while account_A == account_B:
        account_B = random.choice(data)

    print(f"compare A: {format_data(account_A)}")
    print(vs)
    print(f"compare B: {format_data(account_B)}")

    guess = input("Who is more followers?, Type 'A' or 'B' : ").upper()

    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]

    is_correct = check_answer(guess,a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        Should_continue = False

