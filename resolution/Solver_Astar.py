from PIL import Image, ImageDraw

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def is_valid(self, x, y):
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] == '.'

    def solve(self, start, goal):
        # Initialisation de l'algorithme A*
        open_list = []  # Liste des nœuds à traiter (file de priorité)
        closed_list = set()  # Liste des nœuds traités
        parent = {}  # Pour retracer le chemin
        g_values = {}  # Coût réel pour chaque nœud
        f_values = {}  # Coût total estimé pour chaque nœud

        open_list.append(start)
        g_values[start] = 0
        f_values[start] = self.heuristic(start, goal) 

        while open_list:
            current = min(open_list, key=lambda x: f_values[x])
            open_list.remove(current)

            if current == goal:
                # Vous avez trouvé un chemin
                path = [current]
                while current != start:
                    current = parent[current]
                    path.insert(0, current)
                return path

            closed_list.add(current)

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)

                if not self.is_valid(*neighbor) or neighbor in closed_list:
                    continue

                tentative_g = g_values[current] + 1
                if neighbor not in open_list or tentative_g < g_values[neighbor]:
                    parent[neighbor] = current
                    g_values[neighbor] = tentative_g
                    f_values[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    if neighbor not in open_list:
                        open_list.append(neighbor)

        # Aucun chemin trouvé
        return None

    def heuristic(self, current, goal):
        # Heuristique : distance de Manhattan entre les positions actuelle et de destination
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Chemin vers le fichier texte contenant le labyrinthe
maze_file = "resolution/labyrinths/labyrinthe150x150"

# Chargez le labyrinthe depuis le fichier texte
with open(maze_file, 'r') as file:
    maze_str = file.read()

# Transformez la chaîne de caractères en une liste de listes
maze = [list(line) for line in maze_str.strip().split('\n')]

# Créez une instance de MazeSolver
maze_solver = MazeSolver(maze)

# Taille du labyrinthe
n = len(maze)

# Coordonnées de départ et d'arrivée
start = (1, 0)  # Vous avez spécifié (1, 0) comme point de départ
goal = (n - 2, n - 1)  # Vous avez spécifié (n-2, n-1) comme point d'arrivée

# Résolvez le labyrinthe
path = maze_solver.solve(start, goal)

if path:
    # Marquez le chemin sur le labyrinthe
    for x, y in path:
        maze[x][y] = 'o'

    # Affichez le labyrinthe avec le chemin
    for row in maze:
        print(''.join(row))
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
maze_image_before.save("resolution/image_labyrinthe_Astar/maze_before_resolution.jpg")
print("Image du labyrinthe avant la résolution enregistrée sous 'maze_before_resolution.jpg'")

# Après avoir résolu le labyrinthe et obtenu la solution
if path:
    # Créez une image après la résolution du labyrinthe
    maze_image_after = Image.new('RGB', (len(maze[0]) * 20, len(maze) * 20), color='white')
    draw_after = ImageDraw.Draw(maze_image_after)

    # Parcourez le labyrinthe initial pour conserver les murs
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#':
                # Mur
                draw_after.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='black')

    # Marquez le chemin sur l'image après la résolution
    for x, y in path:
        draw_after.rectangle([x * 20, y * 20, (x + 1) * 20, (y + 1) * 20], fill='green')

    # Enregistrez l'image après la résolution
    maze_image_after.save("resolution/image_labyrinthe_Astar/maze_after_resolution.jpg")
    print("Image du labyrinthe après la résolution enregistrée sous 'maze_after_resolution.jpg'")




