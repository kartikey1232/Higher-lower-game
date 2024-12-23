import random
import art
import game_data


size=len(game_data.data)
score=0
while(True):
    print(art.logo)
    player1=random.randint(0,size-1)
    print(f"Compare A: {game_data.data[player1]['name']}, a {game_data.data[player1]['description']}, from {game_data.data[player1]['country']}")
    print(art.vs)
    player2=random.randint(0,50)
    print(f"Against B: {game_data.data[player2]['name']}, a {game_data.data[player2]['description']}, from {game_data.data[player2]['country']}")
    choice=input("Who has more followers? A or B: ").lower();
    if choice == "a":
        if game_data.data[player1]['follower_count'] > game_data.data[player2]['follower_count']:
            score+=1
            print(f"Your are right! Current score: {score}")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif choice == "b":
        if game_data.data[player1]['follower_count'] < game_data.data[player2]['follower_count']:
            score+=1
            print(f"Your are right! Current score: {score}")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break