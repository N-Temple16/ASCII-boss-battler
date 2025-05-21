from utilities.ascii_art import mole
#from game_state import GameState

def initiate_battle_screen(game_state):
    print("Look out for the Giant Mole!")
    print(f"Your stats for the {game_state.combat_style} combat style are as follows: health = {game_state.health}, prayer = {game_state.prayer}, food = {game_state.food}")
    #print(mole)
    return False
