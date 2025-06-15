from models.monster import Monster
from models.base import session  
# CRUD operation

# Add
def add_monsters():
    name = input("Monster Name: ")
    level = int(input("Level: "))
    points = int(input("Points: "))
    monster = Monster(monster=name, level=level, points=points)
    session.add(monster)
    session.commit()
    print(f"Monster '{name}' added.")
    pass
# View
def view_monsters():
    monsters = session.query(Monster).all()
    for m in monsters:
        print(f"{m.id} || {m.monster} || Lvl: {m.level} || Points: {m.points}")

    pass
# Update
def update_monsters():
    mid = int(input("Enter Monster ID: "))
    monster = session.query(Monster).filter_by(id=mid).first()
    if not monster:
        print("Monster not found.")
        return
    monster.monster = input(f"Name ({monster.monster}): ") or monster.monster
    monster.level = int(input(f"Level ({monster.level}): ") or monster.level)
    monster.points = int(input(f"Points ({monster.points}): ") or monster.points)
    session.commit()
    print("Monster updated.")
    pass
# Delete
def delete_monsters():
    mid = int(input("Enter Monster ID: "))
    monster = session.query(Monster).filter_by(id=mid).first()
    if monster:
        session.delete(monster)
        session.commit()
        print("Monster deleted.")
    pass