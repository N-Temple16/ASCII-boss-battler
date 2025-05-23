from utilities.ascii_art import mole
from battle import player_battle_options
from boss import Boss
#from game_state import GameState

def initiate_battle_screen(game_state):
    game_state.load_json_combat_styles()
    boss = Boss("Giant Mole")
    boss.load_boss_json()
    game_state.boss = boss

    print(f"Look out for the {boss.name}!")
    print(mole)
    #print(f"The {boss.name} has arrived, his stats are as follows: health = {boss.health}, ascii = {boss.ascii}, accuracy = {boss.accuracy}, damage range = {boss.damage_range}, combat style = {boss.combat_style}")
    player_battle_options(game_state)
    return False
