import random
import time

# Game constants
WIN_SCORE = 50  # Points required to win
MAX_TURNS = 10  # Maximum allowed turns

def print_pause(text, delay=2):
    """Function to print text with a time delay"""
    print(text)
    time.sleep(delay)

class GameState:
    """Class to manage the game's state and store its variables"""
    def __init__(self):
        """Initialize a new game state"""
        self.reset()
        
    def reset(self):
        """Reset all game variables"""
        self.score = 0  # Player's score
        self.turns_left = MAX_TURNS  # Number of turns left
        self.visited_paths = {  # Dictionary of visited paths
            "left": False,
            "right": False,
            "cave": False,
            "temple": False
        }

def main():
    """Main function that runs the game loop"""
    print_pause("\n=== Welcome to the Magical Forest Adventure! ===")
    print_pause("You wake up in a mysterious forest...")
    print_pause("You look around and see four paths.")
    
    while True:
        game = GameState()
        play_game(game)
        
        if not ask_restart():
            break

def play_game(game):
    """Manages a full single game session"""
    while game.turns_left > 0 and game.score >= 0:
        print(f"\nCurrent score: {game.score}, Turns left: {game.turns_left}")
        
        if game.score >= WIN_SCORE:
            print_pause("⚠️ You've gathered enough power... Dark energy rises...")
            final_battle(game)
            return
            
        if all(game.visited_paths.values()):
            print_pause("You've explored all available paths!")
            final_battle(game)
            return
            
        direction = get_player_choice(game)
        handle_path_choice(direction, game)
        
    if game.score <= 0:
        print_pause("💀 Game over! Your score dropped too low. 💀")
    elif game.turns_left <= 0:
        print_pause("⏰ Game over! Ran out of turns! ⏰")

def ask_restart():
    """Asks the player if they want to play again"""
    while True:
        choice = input("Play again? (y/n): ").lower().strip()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Thanks for playing! 👋")
            return False
        print("Invalid choice. Please type 'y' or 'n'.")

def get_player_choice(game):
    """Handles player's path choice"""
    available_paths = [k for k, v in game.visited_paths.items() if not v]
    
    if not available_paths:
        print_pause("No new paths to explore!")
        return None
    
    prompt = f"Choose a path ({'/'.join(available_paths)}): "
    
    while True:
        choice = input(prompt).strip().lower()
        if choice in available_paths:
            print_pause(f"You chose the {choice} path.")
            game.visited_paths[choice] = True
            return choice
            
        print(f"Invalid choice. Please choose from: {', '.join(available_paths)}")

def handle_path_choice(direction, game):
    """Redirects to the appropriate path function"""
    if direction is None:
        return
        
    if direction == "left":
        left_path(game)
    elif direction == "right":
        right_path(game)
    elif direction == "cave":
        cave_path(game)
    elif direction == "temple":
        temple_path(game)

def left_path(game):
    """Events for the left path"""
    print_pause("\nYou find a locked treasure chest!")
    answer = input("Solve: 3 + 5 = ").strip()
    if answer == "8":
        game.score += 10
        print_pause(f"✅ Correct! +10 points! (Score: {game.score})")
    else:
        game.score -= 5
        print_pause(f"❌ Wrong! -5 points. (Score: {game.score})")
    game.turns_left -= 1

def right_path(game):
    """Events for the right path"""
    print_pause("\nYou meet a wizard who asks a riddle:")
    print_pause("Hint: It's something we use to write, but doesn't unlock anything.")
    answer = input("What has keys but no locks? ").strip().lower()
    if answer in ["keyboard", "piano"]:
        game.score += 15
        print_pause(f"✅ Correct! +15 points! (Score: {game.score})")
    else:
        game.score -= 10
        print_pause(f"❌ Wrong! -10 points. (Score: {game.score})")
    game.turns_left -= 1

def cave_path(game):
    """Events for the cave path"""
    print_pause("\nYou find a glowing mushroom in the cave.")
    choice = input("Do you want to eat it or leave it? (eat/leave): ").strip().lower()
    if choice == "eat":
        if random.random() > 0.5:
            game.score += 20
            print_pause(f"🍄 Magical power! +20 points! (Score: {game.score})")
        else:
            game.score -= 10
            print_pause(f"🤢 Poisoned! -10 points. (Score: {game.score})")
    else:
        print_pause("You wisely avoid the mushroom.")
    game.turns_left -= 1

def temple_path(game):
    """Events for the temple path"""
    print_pause("\nYou discover an ancient temple with a puzzle.")
    print_pause("Hint: This is a basic multiplication problem.")
    answer = input("Solve: 9 × 6 = ").strip()
    if answer == "54":
        game.score += 15
        print_pause(f"✅ Correct! +15 points! (Score: {game.score})")
    else:
        game.score -= 10
        print_pause(f"❌ Wrong! -10 points. (Score: {game.score})")
    game.turns_left -= 1

def final_battle(game):
    """The final battle"""
    print_pause("\n⚔️ You stand before the Dark Wizard, the final boss of your journey!")
    answer = input("What runs but never walks? hint! Water way: ").strip().lower()
    if answer == "river":
        game.score += 30
        print_pause(f"🌟 You defeated the Dark Wizard! +30 points! (Final Score: {game.score})")
    else:
        game.score -= 20
        print_pause(f"💀 The Dark Wizard defeats you! -20 points. (Final Score: {game.score})")

if __name__ == "__main__":
    main()
