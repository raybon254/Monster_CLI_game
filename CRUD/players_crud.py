from models.player import Player
from sqlalchemy.exc import IntegrityError
from models.base import session  
import random, string, re

# Add
def add_player():
    name = input("Enter player's name: ").strip()
    email = input("Enter player's email: ").strip()
    gender = input("Enter player's gender (Male/Female): ").strip().capitalize()
    nick_name = f"{random.choice(string.ascii_uppercase)}{random.randint(1, 100)}"

    # Basic validation
    errors = []
    if not name:
        print(f"Name is required.")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print(f"Invalid email format.")
    if gender not in ["Male", "Female"]:
        print(f"Gender must be 'Male' or 'Female'.")

   

    player = Player(name=name, nick_name=nick_name, email=email, gender=gender)

    session.add(player)
    try:
        session.commit()
        print(f"Player '{name}' added successfully with nickname '{nick_name}'")
    except IntegrityError:
        session.rollback()
        print("A player with this email already exists.")

# View
def view_player():
    players = session.query(Player).all()
    if not players:
        print("No players found.")
        return

    print("\nList of Players:")
    for p in players:
        print(f"Name: {p.name} || Nickname: {p.nick_name} || Email: {p.email} || Gender: {p.gender}")

# Update
def update_player():
    player_name = input("Enter the Name of the player to update: ").strip()
    player = session.query(Player).filter_by(name=player_name).first()

    if not player:
        print("Player not found.")
        return

    name = input(f"New name (current: {player.name}): ").strip() or player.name
    email = input(f"New email (current: {player.email}): ").strip() or player.email
    gender = input(f"New gender (current: {player.gender}): ").strip().capitalize() or player.gender

    # Validate
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return
    if gender and gender not in ["Male", "Female"]:
        print("Gender must be 'Male' or 'Female'.")
        return

    player.name = name
    player.email = email
    player.gender = gender

    try:
        session.commit()
        print(f"Player  {player_name} updated successfully.")
    except IntegrityError:
        session.rollback()
        print("Email already exists.")

# Delete
def delete_player():
    player_name = input("Enter the Name of the player to delete: ").strip()
    player = session.query(Player).filter_by(name = player_name).first()

    if not player:
        print("❌ Player not found.")
        return

    confirm = input(f"Are you sure you want to delete '{player.name}'? (y/n): ").lower()
    if confirm == 'y':
        session.delete(player)
        session.commit()
        print(f"Player '{player.name}' deleted.")
    else:
        print("Cancelled.")

if __name__ == "__main__":
    # add_player()
    # view_player()
    # update_player()
    delete_player()
