from models.base import session
import random

# if prompted - choose level of difficulty
# Display available monster in relation to level play
# Predefine different ai's players and levels

SKILLED = ["Legendbound Champions","Prime Tamers","Mythic Vanguard","Arcane Beastslayers"]

INTERMEDIATE = ["Battleforged Seekers","Elite Trackers","Midnight Claws","Valor Hunters"]

BEGINNER = ["Rookie Wranglers","Novice Nomads","Apprentice Tamers","Freshfang Force"]

# From the level need to map types of attack and attack from monster and attach the level players with different 3 monster per




def level_difficulty():
    print(f"1: BEGINNER")
    print(f"2: INTERMEDIATE")
    print(f"3: SKILLED")
    stage = input("Choose level:")

    if stage == 1:
        random.choice(BEGINNER)
        
        pass
    if stage == 2:
        random.choice(INTERMEDIATE)
        pass
    if stage == 3:
        random.choice(SKILLED)
        pass