from boss import Boss
import random
from utilities.text_colours import TextColours

t = TextColours

def base_player_hit_chance(game_state):
    #calc based on accuracy, combat style, and damage range
    #take a randomly generated number between 1-100, if that number is <= the player's accuracy, a hit is calculated
    #the damage will be anything from the lowest number in damage_range to the highest number
    pass

def base_boss_hit_chance(boss):
    #calc based on accuracy, combat style, and damage range
    #do a check first to see if the player is praying, if so then no damage will be assigned to the player
    #take a randomly generated number between 1-100, if that number is <= the boss's accuracy, a hit is calculated
    #the damage will be anything from the lowest number in damage_range to the highest number
    pass
