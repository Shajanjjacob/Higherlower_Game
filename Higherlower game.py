import database_higherlower_game
import higherloergame_art
import random
import os

score=0
print(higherloergame_art.logo)

def display_accountinfo(account):
    name=account["name"] #account1["name"] replaced with parameter passed 
    description=account["description"]
    country=account["country"]
    return f"{name} a {description} from {country}"

def check_answer(guess,follower_count1,follower_count2):
    if follower_count1>follower_count2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==2:
            return True
        else:
            return False
        
account2=random.choice(database_higherlower_game.data)
continue_flag=True
while continue_flag:#true
        
    #account1=random.choice(database_higherlower_game.data) #frm file name. and list
    account1=account2
    account2=random.choice(database_higherlower_game.data)
    while account1==account2: #if both are same 
        account2=random.choice(database_higherlower_game.data)
        

    print(f"compare1: {display_accountinfo(account1)}")
    print(higherloergame_art.vs)
    print(f"compare2: {display_accountinfo(account2)}")
    #display_accountinfo(account1)
    #display_accountinfo(account2)
    #print(account1) 
    #print(account2) 
    guess=int(input("Who has more follower ?Type 1 or 2:\n"))
    follower_count1=account1["follower_count"]
    follower_count2=account2["follower_count"]

    is_correct=check_answer(guess,follower_count1,follower_count2)
    os.system('cls')
    print(higherloergame_art.logo)

    if is_correct==True:
        score+=1#score=score+1
        print(f"you are right and your score is {score}")
    else:
        print(f"you are wrong and your score is {score}")
        continue_flag=False#exit condition 