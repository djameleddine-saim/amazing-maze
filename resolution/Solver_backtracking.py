from PIL import Image, ImageDraw

# l'algorithme peut résoudre un labyrinthe de 35x35
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def is_valid(self, x, y): 
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze) and self.maze[x][y] == '.' 

    def explore(self, x, y):
        if (x, y) == (len(self.maze) - 1, len(self.maze) - 1):
            return True
        if self.is_valid(x, y):
            self.maze[x][y] = 'o'  # Marquer le chemin
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Droite, Bas, Gauche, Haut
            for dx, dy in directions:
                if self.explore(x + dx, y + dy):
                    return True
            self.maze[x][y] = '*'  # Marquer comme exploré mais non inclus dans le chemin
        return False

    def solve(self):
        if self.explore(1, 0):
            return self.maze  # Le chemin a été trouvé
        else:
            return None  # Aucun chemin trouvé

maze_file = "resolution/labyrinthe/labyrinthe35x35" 
with open(maze_file, 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

# Créer une instance de MazeSolver et résoudre le labyrinthe
maze_solver = MazeSolver(maze)
solution = maze_solver.solve()

if solution:
    for row in solution:
        print(''.join(row))
    print("Chemin trouvé !")
else:
    print("Aucun chemin trouvé.")




# ...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#


# Créez une image avant la résolution du labyrinthe
maze_image_before = Image.new('RGB', (len(maze[0]) * 20, len(maze) * 20), color='white')
draw_before = ImageDraw.Draw(maze_image_before)

# Parcourez le labyrinthe initial et dessinez les murs et les chemins
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == '#':
            # Mur
            draw_before.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='black')
        elif cell == '.':
            # Chemin
            draw_before.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='white')

# Enregistrez l'image avant la résolution
maze_image_before.save("resolution/image_labyrinthe_backtracking/maze_before.jpg")
print("Image du labyrinthe avant la résolution enregistrée sous 'maze_before.jpg'")

# Après avoir résolu le labyrinthe et obtenu la solution
if solution:
    # Créez une image après la résolution du labyrinthe en conservant les murs
    maze_image_after = Image.new('RGB', (len(maze[0]) * 20, len(maze) * 20), color='white')
    draw_after = ImageDraw.Draw(maze_image_after)

    # Parcourez le labyrinthe initial pour conserver les murs
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#':
                # Mur
                draw_after.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='black')

    # Parcourez le labyrinthe résolu et dessinez les cellules explorées et le chemin
    for y, row in enumerate(solution):
        for x, cell in enumerate(row):
            if cell == '*':
                # Cellule explorée mais non incluse dans le chemin
                draw_after.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='gray')
            elif cell == 'o':
                # Cellule faisant partie du chemin
                draw_after.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='green')

    # Enregistrez l'image après la résolution
    maze_image_after.save("resolution/image_labyrinthe_backtracking/maze_after.jpg")
    print("Image du labyrinthe après la résolution enregistrée sous 'maze_after.jpg'")





