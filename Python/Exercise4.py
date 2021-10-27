#6th Question using functions

def rps_game(guess1,guess2,user1,user2):
    if guess1 == guess2:
        print("It's a tie, Try again")
    elif guess1 == "rock":
        if guess2 == "scissor":
            print(user1, "wins,Rock wins")
        else:
            print(user2, "wins,Paper wins")
    elif guess1 == "paper":
        if guess2 == "rock":
            print(user1, "wins,Paper wins")
        else:
            print(user2, "wins,Scissor wins")
    elif guess1 == "scissor":
        if guess2 == "paper":
            print(user1, "wins,Scissor wins")
        else:
            print(user2, "wins,Rock wins")
    else:
        print("Invalid choice, Try again")

user1 = input("enter your name:")
user2 = input("enter your name:")
q = 1
while q > 0:
    print(user1)
    guess1 = input("enter you choice(Rock, Paper, Scissor):").lower()
    print(user2)
    guess2 = input("enter you choice(Rock, Paper, Scissor):").lower()
    game = rps_game(guess1,guess2,user1,user2)
    print(game)
    q = int(input("would you like to continue if yes type 1 else 0:"))
