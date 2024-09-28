def main():
    print("Welcome to the Treasure Hunt Game!")
    print("You are an explorer looking for a mythical treasure in a dense forest.")
    print("You come across a cave which is marked in your map.")
    print("You enter the cave and soon arrive at a junction.")
    print("Do you want to go left or right?")
    user_turn = input(str("Enter: "))
    #option for left
    if user_turn == 'left':
        print("You walk for a few minutes and come face to face with a dragon!")
        print("Now you are dead.")

    elif user_turn == 'right':
        print("You walk for a few minutes and stop in front of a pool of water.")
        print("Do you want to swim across the pool?")
        water_choice = input(str("Enter: "))
        if water_choice == 'yes':
            print("You swim safetly acros the pool and get to the shore.")
            print("You find a strange golden glow at the end of the path.")
            print("Inside a smaller cave, is another pool of water, filled with teasure.")
            print("You find 3 sacks in a corner. Do you want to fill them with the treasure?")
            treasure_choice = input(str("Enter: "))
            if treasure_choice == 'yes':
                print("You jump intp the pool and retrieve the treasure.")
                print("You fill 3 bags with the teasure.")
                print("You have won the game.")   
            elif treasure_choice == 'no':
                print("You decide that you are happy enough to have discovered the treasure and return home happy.")
            else:
                print("Invalid. Choose yes or no.")   
        elif water_choice == 'no':
            print("There is a sudden gust of wind and a dragon comes flying by, knocking you out.")   
            print("You wake up in your bed and realize that it was all just a dream!")
        else:
            print("Invalid. Choose yes or no.")
    else:
        print("Invalid. Choose left or right.")       





if __name__ == "__main__":
    main()
