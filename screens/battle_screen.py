from utilities.ascii_art import mole
#from game_state import GameState

def initiate_battle_screen(game_state):
    game_state.load_json_combat_styles()
    print("Look out for the Giant Mole!")
    print(f"Your stats for the {game_state.combat_style.title()} combat style are as follows: health = {game_state.health}, prayer = {game_state.prayer}, food = {game_state.food}, ascii = {game_state.ascii}, accuracy = {game_state.accuracy}, damage range = {game_state.damage_range}")
    #print(mole)
    return False
