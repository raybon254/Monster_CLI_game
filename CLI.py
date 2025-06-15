from models.base import session
from CRUD.players_crud import add_player, view_player, update_player, delete_player
from CRUD.monsters_crud import add_monsters, view_monsters, update_monsters, delete_monsters
from CRUD.mon_teams_crud import add_mon_teams, view_mon_teams, delete_mon_teams
from CRUD.battle_record import view_all_history,view_player_history
from main import battle
from trades import offer,purchase
from models.session import SessionManager

# User session implementation
session_manager = SessionManager()

def main_menu():
   while True:
      
       if not session_manager.get_current_player():
           print("\n[🔐] You must log in to continue.")
           session_manager.login()
           continue
      
       print("\n====== Main Menu ======")
       print("1. Player Operations")
       print("2. Monster Operations")
       print("3. Monster Team Operations")
       print("4. Battle Field")
       print("5. Trade Monsters")
       print("0. Exit")
       choice = input("Select an option: ").strip()


       if choice == '1':
           player_menu()
       elif choice == '2':
           monster_menu()
       elif choice == '3':
           team_menu()
       elif choice == '4':
           battle_field()
       elif choice == '4':
           trade_monster()
       elif choice == '0':
           print("Goodbye!")
           break
       else:
           print("Invalid option. Try again.")


def player_menu():
   while True:
       print("\n-- Player Menu --")
       print("1. Add Player")
       print("2. View Players")
       print("3. Update Player")
       print("4. Delete Player")
       print("0. Back to Main Menu")
       choice = input("Select an option: ").strip()


       if choice == '1':
           add_player()
       elif choice == '2':
           view_player()
       elif choice == '3':
           update_player()
       elif choice == '4':
           delete_player()
       elif choice == '0':
           break
       else:
           print("Invalid choice.")


def monster_menu():
   while True:
       print("\n-- Monster Menu --")
       print("1. Add Monster")
       print("2. View Monsters")
       print("3. Update Monster")
       print("4. Delete Monster")
       print("0. Back to Main Menu")
       choice = input("Select an option: ").strip()


       if choice == '1':
           add_monsters()
       elif choice == '2':
           view_monsters()
       elif choice == '3':
           update_monsters()
       elif choice == '4':
           delete_monsters()
       elif choice == '0':
           break
       else:
           print("Invalid choice.")


def team_menu():
   while True:
       print("\n-- Team Menu --")
       print("1. Add Monster to Team")
       print("2. View Teams")
       print("3. Delete Team")
       print("0. Back to Main Menu")
       choice = input("Select an option: ").strip()


       if choice == '1':
           add_mon_teams()
       elif choice == '2':
           view_mon_teams()
       elif choice == '3':
           delete_mon_teams()
       elif choice == '0':
           break
       else:
           print("Invalid choice.")

def battle_field():
    while True:
       print("\n⚔️ Battle Field ⚔️")
       print("1. Enter Battle field")
       print("2. View Battle History")
       print("3. View Player History")
       print("0. Back to Main Menu")
       choice = input("Select an option: ").strip()

       if choice == '1':
           battle()
       elif choice == '2':
           view_all_history()
       elif choice == '3':
           view_player_history()
       elif choice == '0':
           break
       else:
           print("Invalid choice.")

def trade_monster():
    while True:
       print("\n⚔️ Trade monster ⚔️")
       print("1. Offer/Sell Monster")
       print("2. Buy/Purchase Monster")
       print("0. Back to Main Menu")
       choice = input("Select an option: ").strip()

       if choice == '1':
           offer()
       elif choice == '2':
           purchase()
       elif choice == '0':
           break
       else:
           print("Invalid choice.")


if __name__ == '__main__':
   main_menu()
