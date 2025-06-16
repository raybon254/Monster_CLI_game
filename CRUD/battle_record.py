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
    
        attacker_name = b.attacker.name if b.attacker else "Unknown"
        defender_name = b.defender.name if b.defender else "Unknown"
        winner_name = b.winner.name if b.winner else "Unknown(pending...)"

        print(f"{b.timestamp} - {attacker_name} vs {defender_name} -> Winner: {winner_name}")

def view_all_history():
    history = session.query(BattleHistory).all()
    for h in history:

        attacker_name = h.attacker.name if h.attacker else "Unknown"
        defender_name = h.defender.name if h.defender else "Unknown"
        winner_name = h.winner.name if h.winner else "Uknown(pending...)"

        print(f"{h.timestamp} - {attacker_name} vs {defender_name} -> Winner: {winner_name}")

    if not history:
        print("No battle records found in the system.")
        return

if __name__ == "__main__":
    view_all_history()