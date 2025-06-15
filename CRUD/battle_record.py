from models.base import session  
from models.battles import BattleHistory

def view_battle_history(player_id):
    battles = session.query(BattleHistory).filter(
        (BattleHistory.attacker_id == player_id) |
        (BattleHistory.defender_id == player_id)
    ).order_by(BattleHistory.timestamp.desc()).all()

    for b in battles:
        print(f"{b.timestamp} - {b.attacker.name} vs {b.defender.name} -> Winner: {b.winner.name}")
