"""Solution to Ellen's Alien Game exercise."""


class Alien:
    # (class)total_aliens_created: int
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate  = x_coordinate 
        self.y_coordinate  = y_coordinate 
        self.health = 3
        Alien.total_aliens_created+=1
        
    def hit(self):
        self.health-=1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate  = new_x_coordinate 
        self.y_coordinate  = new_y_coordinate 

    def collision_detection(self, other):
        pass
        
    
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    aliens = []
    for alien_position in alien_start_positions:
        x, y = alien_position
        a = Alien(x,y)
        aliens.append(a)
    return aliens

