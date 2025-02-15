from game import Game

def get_user_menu_choice():
    while True:
        print("\nWellcome to the menu: the game is simple i think you know how to play good luck.")
        print("(g) Play a new game")
        print("(x) Show scores and exit")
        choice = input(": ").lower().strip()
        if choice in ['g', 'x']:
            return choice
        print("Invalid choice. Please enter 'g' or 'x'.")

def print_results(results):
    print("\nGame Results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("\nThank you for playing.see you soon")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == 'g':
            game = Game()
            result = game.play()
            results[result] += 1
        else:
            print_results(results)
            break

if __name__ == "__main__":
    main()
