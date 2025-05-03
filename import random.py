import random  # For randomness in creature selection and win chances
import time    # To add delays between text outputs for dramatic effect

# Main function that starts and controls the game
def start_game():
    score = 0  # Initialize the player's score

    print("Welcome to the Magical Forest Adventure!")
    time.sleep(2)  # Pause for 2 seconds
    print("Your mission is to find the lost wizard. Your choices and luck will decide your fate.\n")
    time.sleep(2)

    # First choice: which path to take
    choice1 = input("You see two paths: one dark and one bright. Which do you choose? (dark/bright): ").strip().lower()
    time.sleep(1)

    # Handle path choice result
    if choice1 == "dark":
        print("You took the dark path and found a magical scroll! +10 points")
        score += 10  # Gain points
    else:
        print("You took the bright path, but it was full of traps! -5 points")
        score -= 5  # Lose points
    time.sleep(2)

    # Random creature encounter
    creature = random.choice(["a dragon", "a magical wolf", "a friendly genie"])  # Pick a creature randomly
    print(f"\nYou encounter {creature} on your journey!")
    time.sleep(2)

    # Genie gives free bonus
    if creature == "a friendly genie":
        print("The genie gives you a healing spell! +15 points")
        score += 15
    else:
        # Ask player whether to fight or run from the creature
        action = input(f"Do you want to fight the {creature} or run? (fight/run): ").strip().lower()
        time.sleep(1)

        if action == "fight":
            outcome = random.choice(["win", "lose"])  # Randomly decide fight outcome
            if outcome == "win":
                print("You defeated the creature! +20 points")
                score += 20
            else:
                print("You lost the fight... -10 points")
                score -= 10
        else:
            print("You escaped safely, but wasted some time. No points.")
    time.sleep(2)

    # Final stage: try to find the wizard
    print("\nYou reach the wizard's cave...")
    time.sleep(2)

    final_chance = random.randint(1, 10)  # Generate a random number between 1 and 10
    if final_chance > 4:
        # Player wins
        print("You found the lost wizard! 🎉")
        score += 30
        print(f"Congratulations! You won the game with a total score of: {score}")
    else:
        # Player loses
        print("You couldn't find the wizard... Game over.")
        print(f"Your final score was: {score}")
    time.sleep(2)

    # Ask player if they want to play again
    again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if again == "yes":
        print("\n\n--- Restarting the game ---\n\n")
        time.sleep(1)
        start_game()  # Recursively restart the game
    else:
        print("Thanks for playing! See you next time.")

# Start the game when the script runs
start_game()
