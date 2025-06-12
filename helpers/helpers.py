def collect_monster():
    print(f"Choose your starter monster:")
    monster = input("Choose monster")


def explore():
    print(f"You encounter wild monsters in teh Misty Forest!")
    print(f"A wild Sparkbolt(Electric,Rare) appears!")
    print(f"Attempting to catch... Success! {monster} joined your team!")

def battle_wild():
    print(f"Choose your monster for the battle:")
    # print all monster from the particular player(flamewrym,sparkbolt)
    # include the level at the end of the monster(Lv.5)HP:45/45

# then displays the following message
def display():
    print(f"Battle begins!Wild Rockgrinder appears")
    print(f"Battle begins!Wild Rockgrinder appears")


# displays the mechanism that monster uses(fire,tackle,defend,useitem)

def battle_player():
    name = input(f"Enter opponent's username:")
    print(f"Battle request sent to {name}!")

    print("{name} accepts your battle challenge!")
    print("Choose your battle team (up to 3 monsters)")
    # display the monsters to form a team + (Lv.8)

    print(f"⚔️  BATTLE ARENA ⚔️")
    # Displays prompt results in relation to battles
    pass
# create a login and user creation page to facilitate user access


# Validators

# Tables Setup
def players():
    pass
def monster():
    pass
def monster_collection():
    # display seeded date for monster
    # choose
    pass
def leaderboard():
    pass
def recurring_battles():
    pass
def trades():
    pass
def player_progress():
    pass
def statistics():
    pass


# function implementation
def create_battle(player1_id, player2_id, monster_teams) -> dict:    
    pass
def execute_turn(battle_id, attacker_monster, defender_monster, move) -> dict:
    pass
def calculate_damage(attacker_stats, defender_stats, move_power, type_effectiveness) -> int:
    pass
def check_battle_end(battle_id) -> bool:
    pass
def apply_status_effects(monster_id, effect_type) -> None:
    pass

# TRADES
    # A table for trading monsters
    # column for offered and requests
    # perform a request and offer a monster
    # validate if monster needed is avaible based on query
    # Deduct points if request is successfull
    # attach point per monster to be enable deduction
    # Points deducted reflects to whoever offered the monster
def offer_monster(monster):
    return session.query(Trade).filter_by(offer = monster).first()

def request_monster(monster):
    return session.query(Trade).filter_by(request = monster).first()

def player_offer():
    offer = input(f"Enter monster to offer:")
    val_offer = get_monster(offer)
    if not val_offer:
        raise ValueError("Monster not found in your collection")
    print("Monster offered, waiting for a receiver.")

def player_request():
    request = input(f"Enter monster to request:")
    val_request = get_monster(request)
    if not val_request:
        raise ValueError("Monster not found, choose monster available")
    # diplay monster offered with equivalent points
    # From the list of offers enable switch to choose
    # If choice print you are to be deducted {monster's points}
    print("Monster added to your collection")

def propose_trade(from_player, to_player, offered_monsters, requested_monsters):
    # if trade choose offer or request
    # if offer def player_offer
    # if request def player_request



# BATTLES
    # From monster team choose monster
    # define moster attack system
    # randomly choosee attack system for opponent
    # display opponents AI
    # per HP deduct in relation to points mode of attack(fire , water, soil)    
def monsters(monster):
    return session.query(Player).filter_by(monsters = monster).all()

def choose_monster():
    display = session.query(Player).filter_by(monsters = monster).all()





    
    
    
    pass
def calculate_battle_rewards(winner_id, battle_difficulty) -> tuple:
    pass
def create_ai_opponent(difficulty_level) -> dict:
    pass
def catch_monster(player_id, species_id) -> bool:
    pass
def level_up_monster(monster_id) -> dict:
    pass
def get_player_collection(player_id) -> list:
    pass
def calculate_catch_rate(species_rarity, player_level) -> float:
    pass


