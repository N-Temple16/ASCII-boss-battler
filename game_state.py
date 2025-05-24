from boss import Boss
import json

class GameState:
    def __init__(self):
        self.ascii = ""
        self.health = 0
        self.combat_style = ""
        self.accuracy = 0
        self.damage_range = []
        self.prayer = 0
        self.food = 0
        self.boss = None
        self.ispraying = False
        self.praying_against = ""
        self.max_health = 100
        self.max_prayer = 0
    
    def load_json_combat_styles(self):
        with open("data/combat_styles.json") as file:
            data = json.load(file)
        
        if self.combat_style in data:
            stats = data[self.combat_style]
            self.ascii = stats["ascii"]
            self.health = stats["health"]
            self.combat_style = stats["combat_style"]
            self.accuracy = stats["accuracy"]
            self.damage_range = stats["damage_range"]
            self.prayer = stats["prayer"]
            self.food = stats["food"]
            self.max_prayer = stats["prayer"]
        else:
            raise ValueError(f"No data found for combat style: {self.combat_style}")
