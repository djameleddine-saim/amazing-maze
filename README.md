
### Structure des Dossiers
 
amazing-maze/
- **generation/** : Ce dossier contient les scripts et les fichiers liés à la génération de labyrinthes.
  - **__pycache__/** : Ce sous-dossier est généré par Python et contient des fichiers en cache.
  - **backtracking_labyrinths/** : Ce sous-dossier contient les labyrinthes générés avec l'algorithme de backtracking.
  - **kruskal_labyrinths/** : Ce sous-dossier contient les labyrinthes générés avec l'algorithme de Kruskal.
  - **.gitignore** : Ce fichier spécifie les fichiers et dossiers à ignorer lors de la gestion de version avec Git.
  - **case.py** : Ce fichier définit la classe "Case" utilisée pour représenter une case dans un labyrinthe.
  - **labyrinthe.py** : Ce fichier contient la classe principale "Maze" pour générer et afficher les labyrinthes avec les methodes de backtracking et de Kruskal.
  - **main.py** : Ce fichier est le point d'entrée principal de l'application.

- **resolution/** : Ce dossier contient les scripts et les fichiers liés à la résolution de labyrinthes.
  - **image_labyrinthe_Astar/** : Ce sous-dossier contient les images des labyrinthes résolus avec l'algorithme A*.
  - **image_labyrinthe_backtracking/** : Ce sous-dossier contient les images des labyrinthes résolus avec l'algorithme de backtracking.
  - **labyrinths/** : Ce sous-dossier contient les labyrinthes générés.
  - **Solver_Astar.py** : Ce fichier contient la classe "MazeSolver" pour résoudre des labyrinthes avec l'algorithme A*.
  - **Solver_backtracking.py** : Ce fichier contient la classe "MazeSolver" pour résoudre des labyrinthes avec l'algorithme de backtracking.

- **README.md** : Ce fichier est la documentation principale de votre projet, expliquant son fonctionnement, sa structure et comment l'utiliser.
## 1. Introduction
### Contexte du Projet
Le projet de amazing maze a été développé pour générer et résoudre des labyrinthes. Il trouve des applications dans divers domaines tels que les jeux vidéo, la robotique, la planification de mouvement, etc. Notre projet offre une solution complète pour accomplir ces tâches.

### Problématique
La génération et la résolution de labyrinthes sont des tâches complexes nécessitant des algorithmes sophistiqués. Le principal défi de ce projet était de concevoir des algorithmes efficaces pour accomplir ces tâches de manière optimale.

### Objectifs
#### Les principaux objectifs du projet sont :

Implémenter les algorithmes de génération par backtracking et de Kruskal pour créer des labyrinthes.
Mettre en œuvre les algorithmes de résolution par backtracking et A* pour résoudre des labyrinthes.
Fournir une interface utilisateur pour interagir avec le projet.
## 2. Génération de Labyrinthes
### Algorithme de Génération par Backtracking
L'algorithme de génération par backtracking est une méthode pour créer des labyrinthes de manière aléatoire. Il fonctionne en explorant le labyrinthe tout en créant des chemins et en marquant les murs. L'implémentation de cet algorithme est détaillée ci-dessous.

### Algorithme de Génération de Kruskal
L'algorithme de génération de Kruskal repose sur la création d'un arbre de recouvrement minimum dans le labyrinthe. Il mélange aléatoirement les murs tout en maintenant la connectivité.

### Analyse de Complexité


En résumé, l'algorithme de Backtracking récursif peut générer des labyrinthes plus grands  que l'algorithme de Kruskal, qui atteint ses limites plus tôt en raison de sa complexité plus élevée. Cependant, la taille limite exacte dépendra de divers facteurs, notamment les spécifications de système et les performances de machine.


## 3. Résolution de Labyrinthes

### Algorithme de Résolution par Backtracking
L'algorithme de résolution par backtracking est utilisé pour trouver un chemin dans un labyrinthe généré. Il explore le labyrinthe en suivant des règles spécifiques et marque le chemin trouvé.
### Algorithme de Résolution A*
L'algorithme de résolution A* est utilisé pour trouver le chemin le plus court dans un labyrinthe. Il utilise une heuristique pour guider la recherche et trouver rapidement le chemin optimal.

### Analyse de Complexité

#### Algorithme de Backtracking:

- L'algorithme de backtracking explore toutes les possibilités pour résoudre le labyrinthe.
- Sa complexité dépend directement de la taille du labyrinthe et peut être exponentielle.
-  Il peut résoudre efficacement des labyrinthes de petite à moyenne taille jusqu'à 35x35.


#### Algorithme A* :

- L'algorithme A* utilise une approche basée sur l'intelligence artificielle pour trouver le chemin optimal.
- Sa complexité dépend également de la taille du labyrinthe, mais il a généralement une complexité temporelle plus faible que le backtracking.
- Il peut efficacement résoudre des labyrinthes plus grands, et dans mon ce programme, il peut gérer des labyrinthes allant jusqu'à 1000x1000 ou plus en fonction de l'efficacité de l'heuristique utilisée.


#### - Exemple de Génération d'un Labyrinthe en image

![maze_before_resolution](https://github.com/djameleddine-saim/amazing-maze/assets/115147662/fe0b8961-47db-44d2-81f0-7a6fb726c9cf)



#### - exemples de Résolution d'un Labyrinthe

![maze_after_resolution](https://github.com/djameleddine-saim/amazing-maze/assets/115147662/2c7d5816-1097-4960-974d-bf6d1780d5b1)


## Conclusion

Ce projet de génération et de résolution de labyrinthes offre une solution complète pour la création, la résolution et la visualisation de labyrinthes. Il met en œuvre deux algorithmes de génération de labyrinthes, le backtracking et Kruskal, permettant aux utilisateurs de choisir entre des labyrinthes complexes ou aléatoires. De plus, deux algorithmes de résolution, le backtracking et A*, sont inclus pour trouver des chemins dans les labyrinthes générés.
