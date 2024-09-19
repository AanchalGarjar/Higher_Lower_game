import random
import os
import game_art
import H_L_database
print(game_art.logo)
score=0

def display_accountinfo(account):
    name=account['name']
    description=account["description"]
    country=account["country"]
    return f"{name},{description} from {country}"


def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

account_2=random.choice(H_L_database.info)
continue_flag=True
while continue_flag:       

    account_1=random.choice(H_L_database.info)
    account_2=random.choice(H_L_database.info)
    while account_1==account_2:
        account_2=random.choice(H_L_database.info)

    print(f"compare 1: {display_accountinfo(account_1)}")

    print(game_art.vs)
    print(f"compare 2: {display_accountinfo(account_2)}")

    guess=int(input("Who has more followers? 1 or 2: "))
    followers_1=account_1["followers"]
    followers_2=account_2["followers"]
    os.system('cls')
    print(game_art.logo)
    correct_answer=check_answer(guess,followers_1,followers_2)
    if correct_answer==True:
        score+=1
        print(f"you are right.your score is {score}")
    else:
        print(f"you are wrong.your score is {score}")
        continue_flag=False