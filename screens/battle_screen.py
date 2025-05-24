from battle import player_battle_options, clear_screen
from boss import Boss
import os

def initiate_battle_screen(game_state):
    clear_screen()
    game_state.load_json_combat_styles()
    boss = Boss("Giant Mole")
    boss.load_boss_json()
    game_state.boss = boss

    print(f"Look out for the {boss.name}!")
    player_battle_options(game_state)
    return False
