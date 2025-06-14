from player import Player
from monster_team import Team
from trade import Trade
from base import session


def offer():
    player_name = input("Enter your name: ")
    player = session.query(Player).filter_by(name=player_name).first()
    if not player:
        print("Player not found.")
        return

    # Monster teams
    owned_teams = session.query(Team).filter_by(player_id=player.id).all()
    owned_monsters = [team.monster for team in owned_teams]

    if not owned_monsters:
        print("No monsters in your team to offer.")
        return

    print("Your Monsters:")
    for i, mon in enumerate(owned_monsters, 1):
        print(f"{i}. {mon.monster}")

    choice = int(input("Choose a monster to offer by number: "))
    if choice < 1 or choice > len(owned_monsters):
        print("Invalid selection.")
        return

    monster_to_offer = owned_monsters[choice - 1]
    

    # Remove from team
    mon_delete = session.query(Team).filter_by(player_id=player.id, monster_id=monster_to_offer.id).first()
    session.delete(mon_delete)
    session.commit()

    # Reward points
    player.points += 100

    # Save to Trade table
    trade = Trade(monster_id=monster_to_offer.id, offer_by=player.id)
    session.add(trade)
    session.commit()

    print(f"You offered {monster_to_offer.monster}. +100 points added to your account.")  