import json

class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.ascii = ""
        self.accuracy = 0
        self.damage_range = []
        self.attack_types = []

    def load_boss_json(self):
            with open("data/bosses.json") as file:
                bosses = json.load(file)
            
            if self.name in bosses:
                stats = bosses[self.name]
                self.ascii = stats["ascii"]
                self.health = stats["health"]
                self.combat_style = stats["combat_style"]
                self.accuracy = stats["accuracy"]
                self.damage_range = stats["damage_range"]
            else:
                raise ValueError(f"No data found for the boss {self.name}")