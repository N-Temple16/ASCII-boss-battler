from screens.home_screen import show_home_screen
from game_state import GameState

def main():
    game_state = GameState()
    running = True

    while running:
        running = show_home_screen(game_state)

if __name__ == "__main__":
    main()