from models.player import Player
from models.monster_team import Team
from models.trade import Trade
from models.base import session

def purchase():
    buyer_name = input("Enter your name: ")
    buyer = session.query(Player).filter_by(name=buyer_name).first()
    if not buyer:
        print("Player not found.")
        return

    available_trades = session.query(Trade).filter_by(status='open').all()
    if not available_trades:
        print("No monsters available for trade.")
        return

    print("Available Monsters for Purchase:")
    for i, trade in enumerate(available_trades, 1):
        monster = trade.monster
        print(f"{i}. {monster.monster} (Offered by: {trade.offer_player.name})")

    choice = int(input("Choose a monster to purchase by number: "))
    if choice < 1 or choice > len(available_trades):
        print("Invalid selection.")
        return

    selected_trade = available_trades[choice - 1]

    # Confirm purchase
    # Check points sufficiency     
    confirm = input("Confirm purchase for 100 points? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Purchase cancelled.")
        return

    if buyer.points < 100:
        print("Not enough points.")
        return

    # Deduct points from buyer, transfer to offered_by
    buyer.points -= 100
   
    # Update buyer's team
    new_team = Team(player_id=buyer.id, monster_id=selected_trade.monster_id)
    session.add(new_team)

    # Mark trade as sold
    selected_trade.status = 'sold'
    selected_trade.requested_by = buyer.id

    session.commit()
    print(f"Purchase successful! {selected_trade.monster.monster} added to your team.")