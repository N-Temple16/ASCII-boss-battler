class GameState:
    def __init__(self):
        self.health = 100
        self.prayer = 50
        self.food = 5
        self.combat_style = None
    
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