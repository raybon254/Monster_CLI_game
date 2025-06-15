from models.base import session  
from models.monster_team import Team 
from models.player import Player
from models.monster import Monster
# CRUD operation

# Add
def add_mon_teams():
    player_name = input("Player Name: ")
    monster_name = input("Monster Name: ")
    player = session.query(Player).filter_by(name=player_name).first()
    monster = session.query(Monster).filter_by(monster=monster_name).first()
    if not player:
        print("Player not found.")
        return
    if not monster:
        print("Monster not found.")
        return
    team = Team(player_id=player.id, monster_id=monster.id)
    session.add(team)
    session.commit()
    print("Team entry added.")

# View
def view_mon_teams():
    teams = session.query(Team).all()
    for t in teams:
        print(f"Team ID {t.id} || Player: {t.player.name} || Monster: {t.monster.monster}")
    
# Delete
def delete_mon_teams():
    tid = int(input("Enter Team ID to delete: "))
    team = session.query(Team).filter_by(id=tid).first()
    if team:
        session.delete(team)
        session.commit()
        print("Team entry deleted.")
    

# if __name__ == "__main__":
#     # add_mon_teams()
#     # view_mon_teams()
#     delete_mon_teams()