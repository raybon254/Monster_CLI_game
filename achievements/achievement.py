from models.base import session

def level_achievement(player):
    # check players level and validate if its greater than 5 if so award 250 points
    # check players level and validate if its greater than 10 if so award 500 points
    # check players level and validate if its greater than 15 if so award 750 points
    # check players level and validate if its greater than 20 if so award 1050 points

    # From login (current user)- player  ** not supposed to be here initilaized when battling
    # player = SessionManager.get_current_player()
    # if not player:
    #     print("No player logged in.")
    #     return

    awarded = False

    # Player progression
    if player.level >= 2 and player.level < 5:
        player.points += 100
        print("🎉 Level 2 unlocked! +100 points awarded.")
        awarded = True

    elif player.level >= 5 and player.level < 10:
        player.points += 250
        print("🎉 Level 5 unlocked! +250 points awarded.")
        awarded = True

    elif player.level >= 10 and player.level < 15:
        player.points += 500
        print("🎉 Level 10 unlocked! +500 points awarded.")
        awarded = True

    elif player.level >= 15 and player.level < 20:
        player.points += 750
        print("🎉 Level 15 unlocked! +750 points awarded.")
        awarded = True

    elif player.level >= 20:
        player.points += 1050
        print("🎉 Level 20 unlocked! +1050 points awarded.")
        awarded = True

    if awarded:
        session.commit()
    else:
        print("No new achievements unlocked.")