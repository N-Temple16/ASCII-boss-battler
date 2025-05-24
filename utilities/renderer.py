#for health bars I was thinking of doing something like full health [████████], half health [████    ], and a quarter health [██      ]
def draw_bar(label, current, maximum, length = 20):
    filled = int((current / maximum) * length)
    empty = length - filled
    return f"{label}: [{'█' * filled}{'-' * empty}] {current}/{maximum}"