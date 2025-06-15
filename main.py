from models.player import Player
from models.monster import Monster
from models.monster_team import Team
from models.trade import Trade
from trades.offer import offer
from trades.purchase import purchase
from models.battles import BattleHistory
from achievements.achievement import level_achievement
from models.base import session

# kick start session for every function called.
# utility query user
# def get_user(name,nick_name):
#     return session.query(User).filter_by(name=name, nick_name=nick_name).first()




type_effects = {
    "Fire":     {"Ice": 2.0, "Grass": 2.0, "Water": 0.5, "Rock": 0.5},
    "Water":    {"Fire": 2.0, "Rock": 2.0, "Grass": 0.5, "Electric": 0.5},
    "Grass":    {"Water": 2.0, "Soil": 2.0, "Fire": 0.5, "Ice": 0.5},
    "Ice":      {"Grass": 2.0, "Soil": 2.0, "Fire": 0.5, "Rock": 0.5},
    "Electric": {"Water": 2.0, "Ice": 2.0, "Soil": 0.5, "Grass": 0.5},
    "Soil":     {"Electric": 2.0, "Fire": 2.0, "Ice": 0.5, "Grass": 0.5, "Water": 0.5},
    "Normal":   {"Any": 1.0},
    "defend":    {"Fire": 0.7, "Water": 0.5, "Soil": 0.5, "Ice": 0.9, "Electric": 0.9,"Grass": 0.7}
}


attack_type = {
    "1": {"name": "Fire Blast", "type": "Fire", "base_damage": 20},
    "2": {"name": "Tackle", "type": "Normal", "base_damage": 15},
    "3": {"name": "Defend", "type": "defend", "base_damage":1.0},
    "4": {"name":  "Thunderbolt", "type": "Electric", "base_damage": 23},
    "5": {"name": "Aqua Surge", "type": "Water", "base_damage": 17},
    "6": {"name": "Earthquake", "type": "Soil", "base_damage": 25},
    "7": {"name": "Frostbite", "type": "Ice", "base_damage": 21}
}






def calculate_damage(attack_type,defender_type,base_damage):
    damage =type_effects.get(attack_type, {}).get(defender_type, 1.0)
    final_damage = damage * base_damage
    return int(final_damage)


def get_player(name):
    return session.query(Player).filter_by(name=name).first()

def get_teams(player):
    teams = session.query(Team).filter_by(player_id=player.id).all()
    return set(team.monster.monster for team in teams)  


def battle():

    
    print(f"⚔️  BATTLE ARENA ⚔️")

    # Get player names
    player1 = input("Enter player1: ")
    player2 = input("Enter player2: ")

    val_p1 = get_player(player1)
    val_p2 = get_player(player2)

    if not val_p1 or not val_p2:
        raise ValueError("Both players must exist in the database.")
    if val_p1 == val_p2:
        raise ValueError("A player cannot battle themselves.")

    # Get and display teams
    team1 = get_teams(val_p1)
    team2 = get_teams(val_p2)

    if not team1 or not team2:
        raise ValueError("Both players must have at least one monster.")

    print(f"{val_p1.name}'s Monster Team: {team1}")
    p1_team = input("Choose a monster from Player 1's team: ")
    if p1_team not in team1:
        raise ValueError("Invalid monster selection for Player 1.")

    print(f"{val_p2.name}'s Monster Team: {team2}")
    p2_team = input("Choose a monster from Player 2's team: ")
    if p2_team not in team2:
        raise ValueError("Invalid monster selection for Player 2.")

    p1_monster = session.query(Monster).filter_by(monster=p1_team).first()
    p2_monster = session.query(Monster).filter_by(monster=p2_team).first()

    print(f"\n🛎️  Final Battle Recap 🥊")
    print(f"{val_p1.name} VS {val_p2.name}")
    print(f"{p1_team} VS {p2_team}")

    print(f"\nWelcome to the arena!")
    print(f"{p1_team} enters the arena!")
    print(f"{p2_team} enters the arena!\n")

    print(f"======= Player 1 Turn =======")
    print(f"\nWhat will {p1_team} do?")
    for key, atk in attack_type.items():
        print(f"{key}: {atk['name']} ({atk['type']})")

    attack1_choice = input("Choose an attack (1-7): ")
    attack1 = attack_type.get(attack1_choice)
    if not attack1:
        print("Invalid attack choice.")
        return
    print(f"{p1_team} used {attack1['name']}! {attack1['type']}")

    print(f"======= Player 2 Turn =======")
    print(f"\nWhat will {p2_team} do?")
    for key, atk in attack_type.items():
        print(f"{key}: {atk['name']} ({atk['type']})")

    attack2_choice = input("Choose an attack (1-7): ")
    attack2 = attack_type.get(attack2_choice)
    if not attack2:
        print("Invalid attack choice.")
        return
    print(f"{p2_team} used {attack2['name']}! {attack2['type']}")

    print("\n====== DAMAGES======")

    dmg_to_p2 = calculate_damage(attack1['type'], p2_monster.type, attack1['base_damage'])
    dmg_to_p1 = calculate_damage(attack2['type'], p1_monster.type, attack2['base_damage'])

    print(f"{p2_team} takes {dmg_to_p2} damage")
    print(f"{p1_team} takes {dmg_to_p1} damage")

    p2_monster.points -= dmg_to_p2
    p1_monster.points -= dmg_to_p1

    winner = None
    damage_dealt = dmg_to_p2 + dmg_to_p1

    if p2_monster.points <= 0 and p1_monster.points <= 0:
        print("It's a draw! Both monsters fainted.")
    elif p2_monster.points <= 0:
        print(f"{p1_team} wins!")
        val_p1.level += 1
        val_p1.experience += 50
        val_p1.money += 200
        winner = val_p1
        level_achievement(val_p1)

    elif p1_monster.points <= 0:
        print(f"{p2_team} wins!")
        val_p2.level += 1
        val_p2.experience += 50
        val_p2.money += 200
        winner = val_p2
        level_achievement(val_p2)


    else:
        print(f"{p1_team} has points {p1_monster.points}")
        print(f"{p2_team} has points {p2_monster.points}")

    session.commit()

    
    battle_record = BattleHistory(
        attacker_id=val_p1.id,
        defender_id=val_p2.id,
        winner_id=winner.id if winner else None,
        damage_dealt=damage_dealt
    )
    session.add(battle_record)
    session.commit()

    print("Battle data committed.")




# Trade in's

def trade():
    print(f"====== Welcome to the Trade in sector ======")
    print(f"1: Offer a monster.")
    print(f"2: Purchase  a monster.")
    trade = input("Choose a service:")

    if trade == "1":
        offer()
         
    if trade == "2":
        purchase()


if __name__ == "__main__":
    # battle()
    trade()

