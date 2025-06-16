🐉 Monster Collector CLI Game

A terminal-based adventure and management game where players explore, battle, and build monster teams using a robust CLI interface.

Built with Python, SQLAlchemy, and a modular architecture to support scalability and team collaboration.
📦 Features
🎮 Game Mechanics

    Explore Wild Areas – Discover and catch unique monsters.
    Monster Battles – Engage in strategic battles using your custom team.
    Starter Selection – Choose from three elemental monsters.
    Monster Teams – Manage and switch between monster squads.
    Battle History – View past battles and outcomes per player.

👥 Player Management

    Create, view, update, and delete player profiles.
    Login and session tracking via SessionManager.
    View player stats, XP, and collected monsters.

🧠 CLI CRUD Operations

Full terminal-based CRUD support for:

    Players
    Monsters
    Monster Teams
    Battle History

🏗️ Project Structure

Monster_CLI_game/ │ ├── cli.py # Main CLI entry point ├── session_manager.py # Handles login/logout logic │ ├── models/ │ ├── base.py # SQLAlchemy Base and session │ ├── player.py # Player model │ ├── monster.py # Monster model │ └── team.py # Team model │ ├── CRUD/ │ ├── players_crud.py # Player-related CLI actions │ ├── monsters_crud.py # Monster-related CLI actions │ ├── mon_teams_crud.py # Team management │ └── battle_record.py # Battle history │ ├── core/ │ ├── game_engine.py # Exploration and monster catching │ ├── battle_engine.py # Turn-based combat logic │ ├── player_stats.py # Stats, XP, and level management │ └── player_auth.py # Authentication helpers │ ├── requirements.txt └── README.md

yaml Copy Edit
⚙️ Setup Instructions
Fork & Clone the Repository

git clone https://github.com/raybon254/Monster_CLI_game.git
cd Monster_CLI_game
2. Create a Virtual Environment
Using pipenv:

bash
Copy
Edit
pipenv install
pipenv shell

pip install -r requirements.txt

3. Install Dependencies
bash
Copy
Edit
pip install sqlalchemy
pip install faker
pip install alembic
4. Run Alembic Migrations (optional if using migrations)
bash
Copy
Edit
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
🚀 Running the Game
Start the CLI game:

bash
Copy
Edit
python cli.py
You’ll be prompted to log in or create a new player profile.

🧪 Sample Player for Testing
Username: Tester

To create your own player, use Option 1 in the Player Menu.

📌 Dependencies
Python 3.8+

SQLAlchemy

Faker

Alembic

SQLite (default DB)

📜 License
MIT License — free to use, modify, and distribute.
Add any other license

