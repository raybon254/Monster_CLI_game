from models.base import session  
from models.battles import BattleHistory

def view_player_history():
    try:
        player_id = input("Enter player_id:")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return
    
    battles = session.query(BattleHistory).filter(
        (BattleHistory.attacker_id == player_id) |
        (BattleHistory.defender_id == player_id)
    ).order_by(BattleHistory.timestamp.desc()).all()
    if not battles:
        print(f"No battle history found for player ID {player_id}.")
        return

    for b in battles:
        print(f"{b.timestamp} - {b.attacker.name} vs {b.defender.name} -> Winner: {b.winner.name}")

def view_all_history():
    history = session.query(BattleHistory).all()
    for h in history:
        print(f"{h.timestamp} - {h.attacker.name} vs {h.defender.name} -> Winner: {h.winner.name}")

    if not history:
        print("No battle records found in the system.")
        return

if __name__ == "__main__":
    view_all_history()