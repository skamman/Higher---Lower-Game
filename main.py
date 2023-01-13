from art import logo, vs
import random
from game_data import data
from os import system 


game_data = data
print(logo)
score = 0
A = {}
B = {}

def game(score, A, B):
    game_on = True
    while game_on:
        if A == {}:
            A = random.choice(game_data)
            # print(A)
        else:
            pass
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        index_A = game_data.index(A)
        A_follower_count = int(A['follower_count'])
        # print(game_data)
        # print(data)
        B = random.choice(game_data)
        print(f"{vs}")
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
        index_B = game_data.index(B)
        B_follower_count = int(B['follower_count'])
        
        
        choice = input("Who have more followers, type A or B: ")
        #print(f"Choice is {choice}")
        
        if choice == "A":
            if B_follower_count > A_follower_count:
                system('clear')
                print(f"You Loose!! Your score is {score}")
                del game_data[index_A]    
                
                game_on = False
            else:
                system('clear')
                score+=1
                print(f"You Won, Current score: {score}")
                
                
        if choice == "B":
            if B_follower_count < A_follower_count:
                system('clear')
                print(f"You Loose!! Your score is {score}")
                del game_data[index_B]
                game_on = False
            else:
                system('clear')
                score+=1
                print(f"You Won, Current score: {score}")
                A = B
                
        

        
game(score, A, B)
