def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest with two paths.")
    print("One path leads to a quiet village, and the other leads to a mysterious cave.")
    print("Which way do you want to go?")

def village_path():
    print("\nYou walk towards the village.")
    print("As you approach, you see friendly villagers and a cozy inn.")
    print("Do you want to stay at the inn for the night or continue exploring?")
    
    choice = input("Type '1' to stay at the inn or '2' to explore further: ").lower()
    
    if choice == '1':
        print("\nYou decide to stay at the inn.")
        print("The innkeeper offers you a warm meal and a comfortable bed.")
        print("You sleep soundly and wake up refreshed the next morning. You've won!")
    elif choice == '2':
        print("\nYou decide to explore the village further.")
        print("You find a market selling various goods and meet interesting people.")
        print("Suddenly, you discover a hidden map that leads to a treasure. You've won!")
    else:
        print("\nInvalid choice! The adventure ends here.")

def cave_path():
    print("\nYou walk towards the mysterious cave.")
    print("The cave is dark and you can hear strange noises coming from inside.")
    print("Do you want to enter the cave or turn back?")
    
    choice = input("Type '1' to enter the cave or '2' to return to the forest: ").lower()
    
    if choice == '1':
        print("\nYou gather your courage and enter the cave.")
        print("Inside, you find a treasure chest guarded by a sleeping dragon.")
        print("Do you want to try to take the treasure or quietly leave?")
        
        choice = input("Type '1' to take the treasure or '2' to quietly leave: ").lower()
        
        if choice == '1':
            print("\nYou carefully approach the treasure, but the dragon wakes up!")
            print("The dragon is not pleased. Unfortunately, you didn't make it. Game over.")
        elif choice == '2':
            print("\nYou decide not to risk it and quietly leave the cave.")
            print("You safely return to the forest. You've survived!")
        else:
            print("\nInvalid choice! The adventure ends here.")
    elif choice == '2':
        print("\nYou decide that the cave is too dangerous and return to the forest.")
        print("Back in the forest, you find a beautiful clearing where you rest and enjoy nature. You've won!")
    else:
        print("\nInvalid choice! The adventure ends here.")

def start_game():
    intro()
    
    choice = input("Type '1' to go to the village or '2' to go to the cave: ").lower()
    
    if choice == '1':
        village_path()
    elif choice == '2':
        cave_path()
    else:
        print("\nInvalid choice! The adventure ends here.")

if __name__ == "__main__":
    start_game()
