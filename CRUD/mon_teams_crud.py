from models.base import session  
from models.monster_team import Team 
# CRUD operation

# Add
def add_mon_teams():
    player_id = int(input("Player ID: "))
    monster_id = int(input("Monster ID: "))
    team = Team(player_id=player_id, monster_id=monster_id)
    session.add(team)
    session.commit()
    print("Team entry added.")
    pass
# View
def view_mon_teams():
    teams = session.query(Team).all()
    for t in teams:
        print(f"Team ID {t.id} || Player: {t.player.name} || Monster: {t.monster.monster}")
    pass
# Delete
def delete_mon_teams():
    tid = int(input("Enter Team ID to delete: "))
    team = session.query(Team).filter_by(id=tid).first()
    if team:
        session.delete(team)
        session.commit()
        print("Team entry deleted.")
    pass