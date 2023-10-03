import random
import pygame
import os

# Initialize pygame for sound effects
pygame.mixer.init()

# Function to roll the dice
def roll_dice():
    # Play the roll_dice sound effect
    pygame.mixer.music.load("sounds/roll_dice.mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass

    # Simulate rolling the dice
    result = random.randint(1, 6)
    
    # Display the result
    print(f"You rolled a {result}")

    # Play the ding sound effect
    pygame.mixer.music.load("sounds/ding.mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pass

def main():
    while True:
        print("Press 'Enter' to roll the dice or 'q' to quit.")
        choice = input(": ")

        if choice == "q":
            break
        elif choice == "":
            roll_dice()
        else:
            print("Invalid input. Please press 'Enter' to roll the dice or 'q' to quit.")

if __name__ == "__main__":
    # Set the working directory to the project folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Call the main function to start the program
    main()
