from faker import Faker
from models.player import Player
from models.monster import Monster
from models.monster_team import Team
from models.base import drop_table, create_table,session
import random
import string

def seed_data():
    print(f"Seeding Data...!")
    drop_table()
    create_table()

    fake = Faker()   

    players = []
    for _ in range(5):
        gender = random.choice(["male", "female"])
        nickname = f"{random.choice(string.ascii_uppercase)}{random.randint(1,100)}"
        player = Player(
            name = fake.name(),
            nick_name = nickname,
            email = fake.email(),
            gender = gender
        )
        session.add(player)
        players.append(player)
        session.commit()    

    monsters = []
    for _ in range(10):
        monst = ["flamewyrm","Aquafin","Vinewhip","Sparkbolt","Rockgrinder","Gusthawk","Noxshade"]
        monster = Monster(
            monster = random.choice(monst),
            level = 1,
            points = 50
        )
        session.add(monster)
        monsters.append(monster)
        session.commit()    

    teams = []
    for _ in range(10):
        player = random.choice(players)
        monster = random.choice(monsters)
        team = Team(
            player_id = player.id,
            monster_id = monster.id
        )
        session.add(team)
        teams.append(team)
        session.commit()    

    print(f"Seeding Data complete!")

if __name__ == '__main__':
    seed_data()