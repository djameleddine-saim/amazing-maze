import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = {'N': True, 'E': True, 'S': True, 'W': True}

    def break_wall(self, direction, next_case):
        opposit_dir = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        self.wall[direction] = False
        next_case.wall[opposit_dir[direction]] = False

    def check_walls(self): 
        if False in self.wall.values():
            return False
        else:
            return True

class Maze:
    def __init__(self, name): 
        self.name = name
        self.n = int(input("Entrez la taille du labyrinthe (N): "))
        self.board = [[Case(x, y) for x in range(self.n)] for y in range(self.n)] 

    def get_neighbour(self, cell):
        x, y = cell.x, cell.y 
        directions = ['N', 'E', 'S', 'W']
        random.shuffle(directions)  # Mélange aléatoire des directions
        for dir in directions: 
            if dir == 'N' and y > 0: 
                next_cell = self.board[y - 1][x] 
            elif dir == 'E' and x < self.n - 1: 
                next_cell = self.board[y][x + 1]
            elif dir == 'S' and y < self.n - 1:
                next_cell = self.board[y + 1][x]
            elif dir == 'W' and x > 0:
                next_cell = self.board[y][x - 1]
            else:
                continue
            if next_cell.check_walls():
                return next_cell, dir
        return None

    def generate_maze_backtracking(self):
        
        stack = [self.board[0][0]]
        while stack:
            current_cell = stack[-1]
            next_cell_info = self.get_neighbour(current_cell)
            if next_cell_info:
                next_cell, dir = next_cell_info
                current_cell.break_wall(dir, next_cell)
                stack.append(next_cell)
            else:
                stack.pop()


    def generate_maze_Kruskal(self):
        pass

    def display(self):
        filename = input("Entrez le nom du fichier pour sauvegarder le labyrinthe : ")
        with open(filename, 'w') as file:
            for y in range(self.n):
                for x in range(self.n):
                    if self.board[y][x].wall['N']:
                        file.write("+---")
                    else:
                        file.write("+   ")
                file.write("+\n")
                for x in range(self.n):
                    if self.board[y][x].wall['W']:
                        file.write("|   ")
                    else:
                        file.write("    ")
                file.write("|\n")
            for x in range(self.n):
                file.write("+---")
            file.write("+\n")




maze = Maze("My Maze")
maze.generate_maze_Kruskal()  # Génération du labyrinthe
maze.display()  # Affichage du labyrinthe

