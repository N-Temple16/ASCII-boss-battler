import json

class GameState:
    def __init__(self):
        self.ascii = ""
        self.health = 0
        self.combat_style = ""
        self.accuracy = 0
        self.damage_range = (0, 0)
        self.prayer = 0
        self.food = 0
    
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
        else:
            raise ValueError(f"No data found for combat style: {self.combat_style}")


    def apply_combat_style_modifiers(self):
        match self.combat_style:
            case "magic":
                self.health = 80
                self.prayer = 90
                self.food = 8
            case "range":
                self.health = 90
                self.prayer = 75
                self.food = 7
            case "melee":
                self.health = 100
                self.prayer = 60
                self.food = 6