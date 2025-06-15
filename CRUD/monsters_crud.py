from models.monster import Monster
from models.base import session  
import random
# CRUD operation

# Add
def add_monsters():
    monster_pool = [
        {"name": "Flamewyrm", "type": "fire"},
        {"name": "Aquafin", "type": "water"},
        {"name": "Vinewhip", "type": "grass"},
        {"name": "Sparkbolt", "type": "electric"},
        {"name": "Rockgrinder", "type": "rock"},
        {"name": "Gusthawk", "type": "flying"},
        {"name": "Noxshade", "type": "dark"},
    ]
    name = input("Monster Name: ")
    mon_type = random.choice(monster_pool)
    type_power = mon_type["type"]
    monster = Monster(monster=name, type_power=type_power)
    session.add(monster)
    session.commit()
    print(f"Monster '{name}' added.")
    
# View
def view_monsters():
    monsters = session.query(Monster).all()
    for m in monsters:
        print(f"{m.id} || {m.monster} || Lvl: {m.level} || Points: {m.points}")

    
# Update
def update_monsters():
    mid = int(input("Enter Monster Name: "))
    monster = session.query(Monster).filter_by(monster=mid).first()
    if not monster:
        print("Monster not found.")
        return
    monster.monster = input(f"Name ({monster.monster}): ") or monster.monster
    monster.level = int(input(f"Level ({monster.level}): ") or monster.level)
    monster.points = int(input(f"Points ({monster.points}): ") or monster.points)
    session.commit()
    print("Monster updated.")
    
# Delete
def delete_monsters():
    name = input("Enter Monster Name: ")
    monster = session.query(Monster).filter_by(monster=name).first()
    if monster:
        session.delete(monster)
        session.commit()
        print("Monster deleted.")
    else:
        print("Monster not found.")

# if __name__ == "__main__":
#     add_monsters()
#     # view_monsters()
#     # update_monsters()
#     # delete_monsters()
    