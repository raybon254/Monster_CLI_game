from sign_in import User
from player import Player
from monster import Monster
from monster_team import Team
from base import session

# utility qurey user
# def get_user(name,nick_name):
#     return session.query(User).filter_by(name=name, nick_name=nick_name).first()

# def login():
#     name = input("Enter your Name:")
#     nick_name = input("Enter your nickname:")

#     res = get_user(name,nick_name)
#     if res:
#         print(f"Successfully logged in!")
#     else :
#         print(f"Invalid credentials")

def get_player(name):
    return session.query(Player).filter_by(name=name).first()

def get_teams(player):
    teams = session.query(Team).filter_by(player_id=player.id).all()
    return set(team.monster.monster for team in teams)  

def attacks():
    print(f"1. Fire Blast (Strong vs Rock!)")
    print(f"2. Tackle (Normal damage)")  
    print(f"3. Defend (Reduce incoming damage)")
    print(f"4. Use Item")

def items():
    print(f"1. Thunderbolt (Strong vs Water!)")
    print(f"2. Aqua Surge (Strong vs Soil!)")
    print(f"3. Earthquake (Strong vs Electric!)")
    print(f"4. Frostbite (Strong vs Air!)")

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

    # Battle starts
    print(f"\nWelcome to the arena!")
    print(f"{p1_team} enters the arena!")
    print(f"{p2_team} enters the arena!\n")

    # Player 1 attack
    print(f"\nWhat will {p1_team} do?")
    attacks()
    pick = input("Choose an attack (1-4): ")
    
    if pick == "1":
        print(f"{p1_team} used Fire Blast! 🔥")
    elif pick == "2":
        print(f"{p1_team} used Tackle! 💥")
    elif pick == "3":
        print(f"{p1_team} used Defend! 🛡️")
    elif pick == "4":
        items()
        pick2 = input("Choose a special item attack (1-4): ")
        if pick2 == "1":
            print(f"{p1_team} used Thunderbolt! ⚡ (Strong vs Water!)")
        elif pick2 == "2":
            print(f"{p1_team} used Aqua Surge! 💧 (Strong vs Soil!)")
        elif pick2 == "3":
            print(f"{p1_team} used Earthquake! 🌍 (Strong vs Electric!)")
        elif pick2 == "4":
            print(f"{p1_team} used Frostbite! ❄️ (Strong vs Air!)")
        else:
            print("Invalid special attack.")
    else:
        print("Invalid attack choice.")


    # Player 2 attack
    print(f"\nWhat will {p2_team} do?")
    attacks()
    pick = input("Choose an attack (1-4): ")
    
    if pick == "1":
        print(f"{p2_team} used Fire Blast! 🔥")
    elif pick == "2":
        print(f"{p2_team} used Tackle! 💥")
    elif pick == "3":
        print(f"{p2_team} used Defend! 🛡️")
    elif pick == "4":
        items()
        pick2 = input("Choose a special item attack (1-4): ")
        if pick2 == "1":
            print(f"{p2_team} used Thunderbolt! ⚡ (Strong vs Water!)")
        elif pick2 == "2":
            print(f"{p2_team} used Aqua Surge! 💧 (Strong vs Soil!)")
        elif pick2 == "3":
            print(f"{p2_team} used Earthquake! 🌍 (Strong vs Electric!)")
        elif pick2 == "4":
            print(f"{p2_team} used Frostbite! ❄️ (Strong vs Air!)")
        else:
            print("Invalid special attack.")
    else:
        print("Invalid attack choice.")

    # Final Summary
    print(f"\n🛎️  Final Battle Recap 🥊")
    print(f"{val_p1.name} VS {val_p2.name}")
    print(f"{p1_team} VS {p2_team}")
    print("Battle completed (damage calculations not yet implemented).")
    # based on level increment [per win] and points deductions 


if __name__ == "__main__":
    battle()

