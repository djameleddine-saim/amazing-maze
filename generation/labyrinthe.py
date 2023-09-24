import random
import os
from case import Case

class Maze:
    def __init__(self, name): 
        self.name = name
        self.n = int(input("Entrez la taille du labyrinthe (N): "))
        self.board = [[Case(x, y) for x in range(self.n)] for y in range(self.n)] 

        self.output_directory_backtracking = "generation/backtracking_labyrinths"  # Dossier pour les labyrinthes Backtracking
        self.output_directory_kruskal = "generation/kruskal_labyrinths"  # Dossier pour les labyrinthes Kruskal

        # Créez les dossiers s'ils n'existent pas
        os.makedirs(self.output_directory_backtracking, exist_ok=True)
        os.makedirs(self.output_directory_kruskal, exist_ok=True)

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
        # Créez une liste de toutes les parois avec leur état initial
        walls = []
        for y in range(self.n):
            for x in range(self.n):
                if x > 0:
                    walls.append((self.board[y][x], self.board[y][x - 1], 'W'))
                if y > 0:
                    walls.append((self.board[y][x], self.board[y - 1][x], 'N'))

        # Mélangez aléatoirement la liste des parois
        random.shuffle(walls)

        # Utilisez un ensemble disjoint pour suivre les composants connectés (ensembles de cellules)
        sets = {cell: {cell} for row in self.board for cell in row}

        # Fonction pour trouver l'ensemble auquel appartient une cellule
        def find_set(cell):
            for set, cells in sets.items():
                if cell in cells:
                    return set

        # Itérez sur les parois mélangées et appliquez l'algorithme de Kruskal
        for wall in walls:
            cell1, cell2, direction = wall
            set1 = find_set(cell1)
            set2 = find_set(cell2)

            if set1 != set2:
                cell1.break_wall(direction, cell2)
                # Fusionnez les ensembles
                sets[set1] |= sets[set2]
                del sets[set2]

                # Attribution d'un numéro unique à toutes les cellules du nouvel ensemble
                for cell in sets[set1]:
                    cell.ID = set1.ID

    def display(self, algorithm):
        
        filename = input(f"Entrez le nom du fichier pour sauvegarder le labyrinthe ({algorithm}): ")
        
        # Déterminez le répertoire de sortie en fonction de l'algorithme
        output_directory = (
            self.output_directory_backtracking if algorithm == "Backtracking" else self.output_directory_kruskal
        )

        file_path = os.path.join(output_directory, filename)
        with open(file_path, 'w') as file:
            maze_display = [["#" for _ in range(2 * self.n + 1)] for _ in range(2 * self.n + 1)]
            for row in range(self.n):
                for col in range(self.n):
                    maze_display[2 * row + 1][2 * col + 1] = "."
                    if self.board[row][col].wall['N']:
                        maze_display[2 * row][2 * col + 1] = "#"
                    else:
                        maze_display[2 * row][2 * col + 1] = "."
                    if self.board[row][col].wall['S']:
                        maze_display[2 * row + 2][2 * col + 1] = "#"
                    else:
                        maze_display[2 * row + 2][2 * col + 1] = "."
                    if self.board[row][col].wall['W']:
                        maze_display[2 * row + 1][2 * col] = "#"
                    else:
                        maze_display[2 * row + 1][2 * col] = "."
                    if self.board[row][col].wall['E']:
                        maze_display[2 * row + 1][2 * col + 2] = "#"
                    else:
                        maze_display[2 * row + 1][2 * col + 2] = "."
            
            maze_display[1][0] = "."
            
            maze_display[2 * self.n - 1][2 * self.n] = "."
            maze_str = ""
            for line in maze_display:
                maze_str += "".join(line) + "\n"
            file.write(maze_str)
        print(f"Le labyrinthe a été enregistré dans {file_path}")


