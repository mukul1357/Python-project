def enemycollide(eX, eY, pX, pY):
    if eX - pX <= 50 and pX - eX <= 30 and eY - pY <= 160 and pY - eY <= 70:
        # returns true if the Enemy robots and player seems to be touching each other
        return True
    return False

def obstaclecollide(oX, oY, pX, pY):
    if oX - pX <= 50 and pX - oX <= 40 and oY - pY <= 175:
        # returns true if the Obstacles and player seems to be touching each other
        return True
    return False

def dodge_fail(bX, bY, pX, pY):
    distanceY = bY - pY
    distanceX = bX - pX
    if distanceX < 70 and distanceX > 20 and distanceY > 20 and distanceY < 170 and bX >= 0:
        # returns true if the enemy's energy balls and player seems to be touching each other
        return True
    return False

# checking for locations
def decide_location(score):
    # returns the location number based upon the score passed and pre-decided requirements to cross each location
    if score < 1000:
        return 1
    elif score in range(1000, 2000):
        return 2
    elif score in range(2000, 4500):
        return 3
    elif score >= 4500:
        return 4

# FUNCTION FINDING WHETHER HERO'S BULLET HIT THE ENEMY ROBOTS
def shoot_success(enemyX, enemyY, bulletX, bulletY, shoot):
    distanceY = enemyY - bulletY
    distanceX = enemyX - bulletX
    if distanceY < 120 and distanceY > 0 and distanceX < 1 and shoot and bulletX <= 1150:
        # returns true if the enemy and player's bullet seems to be touching each other
        return True
    return False