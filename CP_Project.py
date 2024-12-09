from Stat_Sheet import * #Charater and items import
from Test_fight import *
from Test_fight import apply #fighting
def start_up(): # start menu for help
    print("Welcome to Forest of Kel!")
    choice = input("What do You need?(How to play/ Start/ Stop):").lower() #inputs here no hidden ones
    if choice == "how to play":
        print("You play by inputing words to do actions.")
        print("EXAMPLE: 'grab rope' will add rope.")
        print("However, the inputs are area exclusive, so DO NOT SPAM THEM!")
        print ("Your choices will decide your fate in the Forest of Kel. GOOD LUCK!")
        start_up()
    elif choice == "start":
        player_spawn(player_one)
    elif choice == "stop":
        print("Thanks for Playing!")
    else:
        print("Oops that input is useless try another.")
        start_up()

#start the game
def player_spawn(player_one):

    print("You are lost in forest.")
    print("you see three paths ahead")
    print("North is the Mountain, West to the Lake, East to the Valley.")

    choice = input("Onward. (North/West/East): ").lower() #inputs to send player into game
    
    if choice == "north":
        mountain()
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        player_spawn(player_one)
#Forest return Loc to spawn axe
def forest():
    print("You are back in the forest")
    if axe in player_one.inventory:
     pass
    else:
     print("You see an axe leaning on the tree.")
    choice = input("Onward. (North/West/East):").lower()
    if choice == "north":
        mountain()
    elif choice == "grab axe":#axe checks
        print ("You try to grab the axe")
        if axe in player_one.inventory:
            print("You have that")
            forest()
        elif axe not in player_one.inventory: 
             print("you grab axe.")
             player_one.inventory.append(axe)
             forest()
        else:
            pass
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        forest()
#Mountain Loc
def mountain():
    print("You are in the Mountain")
    print("You see a House and some rock")
    print("Along with two road to the lake and valley")
    if rope in player_one.inventory: #rope spawn
     pass
    else:
     print("You see a rope hanging from a tree")
    
    choice = input("Now what? (Head Back/Enter House/ Climb Rocks/ Go to lake/ Go to valley): ").lower()
 #the locs choices
    if choice == "go to valley":
        print("To the Valley")
        valley()
    elif choice == "go to lake":
        print("To the Lake")
        lake()
    elif choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "enter house":
        print("the door is locked.")
        #entering house checks
        if  boards in player_one.inventory:
            print("However, You enter the house through a nice hole.")
            house()
        elif axe in player_one.inventory:
         print("Do you want to cut down the locked door")
         choice = input("(Yes/ No):").lower()
         if choice == ("yes"):
             print("You cut down the door.")
             player_one.inventory.append(boards)
             house()
         else:
             print("You head back")
             mountain()
        else:
         print("You turn back")
         mountain()
    elif choice=="climb  rocks": #death
        print("rock time")
        print('You climb to a cliff edge. You meet God and become wise.')
        print('Now you do not need to escape. Game Over!')
        stop()
    elif choice == "grab rope":#rope inputs hidden to make players think
        print ("You try to grab the rope")
        if rope in player_one.inventory:
            print("You have that")
            mountain()
        elif rope not in player_one.inventory: 
             print("you grab rope.")
             player_one.inventory.append(rope)
             mountain()
        else:
            pass
    else:
        print("You know you are wrong")
        mountain() #loop if input is inncorrect
#the house Loc  
def house():
    print("You enter the house.")
    print("You see an old man.")#npc
    
    choice = input("Now what? (Talk to Old Man/ Head back):").lower()
#inputs
    if choice == "head back":
        print("You go back")
        mountain()
    elif choice == "talk to old man":
        print("You approch old man")
        print("Hello young umm them?")
        man_speak()
    else:
        print("You know you are wrong")
        house()    
#Lake Loc
def lake():
    print('You arrive at the Lake.')
    print("You see a road to the Mountain.")
    if boat in player_one.inventory:
        pass
    else:
     print("You see a boat floating.")
    choice = input("(Head Back/go to road):").lower()
    
    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "throw rope":
     print("you throw the rope on the boat")
     if rope in player_one.inventory and player_one.arm >3:
         print("You got the boat")
         player_one.inventory.append(boat)
         lake()
     else:
         print("you failed to throw")
         lake()
    elif choice == "go to road":
        print("You walk up the road.")
        mountain()
    elif choice == "sail home":
        if boat in player_one.inventory:
            choice = input("(Yes/No):").lower()
            if choice =="yes":
             print("You sail home.")
             apply()
             main() 
            elif choice == "no":
                print("You get out of the boat and drown. GAME OVER!") 
                stop()
        else:
            print("You fall into the water and sink deep down. GAME OVER!")
            stop()
    else:
        print("You know you are wrong.")
        return lake() 
#Valley area
def valley():
    print("You arrive to the Valley.")
    print("It is a sea of green grass and bush with berries.")
    if map in  player_one.inventory:
        print("The map shows da way")
        pass

    choice = input("(Head Back/Take Mountain Road /Go to the Green Sea):").lower()
    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "take mountain road":
        mountain()
    elif choice == "grab berries":
        player_one.inventory.append(berries)
        print("you grab berries")
        return valley()
    elif choice == "go da way":
        print("You found da way")
        finish_line()
    elif choice == "go to the green sea":
        print("You walk into the sea lost forever. GAME OVER")
        stop()
    else:
        print("You know You are wrong")
        return valley()
#NPC speech
def man_speak():
    print("You have come for my map")
    if map in player_one.inventory:
        print("You have taken the map. Go to the valley to leave.")
        house()
        pass
       
    choice = input("(Yes/ No):").lower()
    if choice== "yes":
        print("Bring me berries and the map is yours.")
        pass
    elif choice== "no":
        print("okay? Then leave.")
        print("He is done talkin.")
        house()
    elif choice== "you are old":
        print("Well you suck.")
        print("He is done talkin.")
        house()
    else:
        print("What are you talking about")
        return man_speak()
    if berries in player_one.inventory:
        print("Thank You. Here is the map.")
        player_one.inventory.append(map)
        print("He eats the berriers and smiles")
        house()
    else:
        print("Get the berries.")
        house()
#Victory Message
def finish_line():
     print("You are the Master of Game.")
     stop()
#game loop
def stop():
    print("Do you want to play again?")
    choice = input("(Play again/Stop playing):").lower()
    if choice == "play again":
        player_spawn(player_one)
    elif choice == "stop playing":
        print("Thanks for Playing")
    else:
        print("What?")
        stop()
#Start call  
if __name__ == "__main__":
    start_up()
