# ASCII-boss-battler
A turn based combat game played in the terminal with inspiration from games such as Runescape and Pokemon.

## How to Run
1. Install Python from the official Python website
2. Clone the provided repo using: ```git clone https://github.com/N-Temple16/ASCII-boss-battler.git```
3. Run the game by using either ```python main.py``` or ```python3 main.py```, located at the base of the project

## How to Play
As mentioned, this is a turn based combat game played within the terminal. The goal is to simply defeat the boss, although the challenge lies in the fact that you cannot ONLY attack the boss each turn and will need to strategically plan out your moves.

### Gear Setup
Once you start you will be presented with a choice, what combat style you would like to take on the boss with. To make sure you are certain about the choice, you are given the stats and information about each style so that you know what you are getting into.

![image](https://github.com/user-attachments/assets/36c70bbf-9236-4d58-8992-db3557a4e2af)

A boss is not inheritantly weak to one certain combat style, so choose whatever style you feel would work the best.

### Battle
As soon as you have chosen your desired combat style you will be put into the boss fight. Currently there is one main boss in the game known as "The Giant Mole" and I am looking to add more bosses in the future, each with their own unique mechanics.
You will be presented with a similar list of options as before but this time with combat mechanics. To briefly go through each:
1. `Attack` is as simple as it sounds, you attack the boss and will roll your hit using your style's accuracy and damage range. There is a chance to miss your attack as well if you miss your accuracy check
2. `Protecting from Magic, Range and Melee` are similar to "Prayers" in Runescape where you can protect yourself from the boss's incoming combat style which is indicated in the chat. You are only able to protect for a certain amount of turns as this is limited by the amount of prayer you have. Once activated, each turn uses 15 prayer and will protect you until you either run out of prayer or you toggle your protection off
3. `Stop protecting` is how you can cancel your current protection against a style. This is useful if you only want to protect yourself for a turn or two to heal and don't want to completely use up your prayer
4. `Eat Food` is how you can heal from the boss's attacks

![image](https://github.com/user-attachments/assets/0a412192-ef25-44c5-9e6e-ada26944966f)

Now from this, you and the boss will go through a back and forth battle to see which one comes out on top. Good luck!

## Roadmap
- More bosses, each with different mechanics that you will have to correctly handle (more than one combat style, maybe a one-shot mechanic that must be blocked or you lose immediately)
- Time trials or speedrun capabilities
- A leveling system after each boss
