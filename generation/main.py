from labyrinthe import Maze
#import timeit
#import cProfile

def choose_generation_algorithm(maze):
    print("Choisissez l'algorithme de génération du labyrinthe :")
    print("1. Récursive Backtracking")
    print("2. Kruskal")
    choice = input("Entrez le numéro de l'algorithme choisi : ")
    if choice == "1":
        maze.generate_maze_backtracking()
        maze.display("Backtracking")
    elif choice == "2":
        maze.generate_maze_Kruskal()
        maze.display("Kruskal")
    else:
        print("Choix invalide. Veuillez choisir 1 pour Récursive Backtracking ou 2 pour Kruskal.")

# Créez une instance de Maze
maze = Maze("My Maze")

# Demandez à l'utilisateur de choisir l'algorithme de génération
choose_generation_algorithm(maze)

#cProfile.run('maze.generate_maze_Kruskal()')
#cProfile.run('maze.generate_maze_backtracking()')