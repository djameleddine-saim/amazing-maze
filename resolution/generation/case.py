
class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = {'N': True, 'E': True, 'S': True, 'W': True}
        self.ID = None  # Ajouter un attribut pour stocker le numéro de l'ensemble

    def break_wall(self, direction, next_case):
        opposit_dir = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        self.wall[direction] = False
        next_case.wall[opposit_dir[direction]] = False

    def check_walls(self): 
        if False in self.wall.values():
            return False
        else:
            return True
