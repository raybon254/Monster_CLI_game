from models.base import session  
from models.monster_team import Team 
# CRUD operation

# Add
def add_mon_teams():
    player_name = int(input("Player Name: "))
    monster_name = int(input("Monster Name: "))
    team = Team(player_id=player_name.id, monster_id=monster_name.id)
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

if __name__ == "__main__":
    add_mon_teams()
    # view_mon_teams()
    # update_mon_teams()
    # delete_mon_teams()