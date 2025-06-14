from player import Player
from base import session

class SessionManager:
    def __init__(self):
        self.current_player = None

    def login(self):
        name = input("Enter your name: ")
        player = session.query(Player).filter_by(name=name).first()
        if player:
            print(f"Logged in as {player.name}")
            self.current_player = player
        else:
            print("Player not found.")

    def logout(self):
        self.current_player = None
        print("Logged out.")

    def get_current_player(self):
        return self.current_player
