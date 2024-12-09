from Stat_Sheet import * 

def apply():
    print("You see something in the water")
    print("A Great Dragon rises out of the water")
    if axe in  player_one.inventory:
     print("You rasie the Axe in the air")
     player_one.arm_pump(axe)
   
def get_computer_choice():
    choices = ["strike", "dodge", "fake"]
    com_choice=None
    if com_choice == "strike":
        com_choice = "dodge"
    elif com_choice == "dodge":
        com_choice = "fake"
    else:
        com_choice = "strike" 
    return com_choice # failed cycling randomization
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "strike" and computer_choice == "fake") or \
         (player_choice == "fake" and computer_choice == "dodge") or \
         (player_choice == "dodge" and computer_choice == "strike"):
        return "player"
    else:
        return "computer"

def main():
    player_one.health
    water_dragon.health 
    
    print("Welcome to the fight")
    print("Both players start with 100 health points. Lose a round, lose health. First to 0 health loses the fight!")
    print("Let the fight, Begin!")

    while player_one.health > 0 and water_dragon.health > 0:
        player_choice = input("Enter your choice (strike, dodge, fake): ").lower()

        if player_choice not in ["strike", "dodge", "fake"]:
            print("Invalid choice! Please choose strike, dodge, or fake.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        

        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie! No health lost.")
        elif result == "player":
            water_dragon.health -= player_one.arm
            print(f"You win this round! Great Dragon loses:" f"{player_one.arm}" " Dragon's health:" f"{water_dragon.health}")
        else:
            player_one.health -= water_dragon.arm
            print(f"You lose this round! You lose:"f"{water_dragon.arm}" " Your health:" f"{player_one.health}")

    # Check who won
    if player_one.health == 0:
        print("You are out of health! Great Dragon wins! GAME OVER!")
    else:
        print("The Great Dragon is out of health! Congratulations, You win!")

if __name__ == "__main__":
 apply()
 main()
    
