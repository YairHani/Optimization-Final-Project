import numpy as np
import sys
from Graph import Graph
from Game import Game
matrix_of_neighbors = [
    [1, 0, 11, 0, 0, 7, 0, 4, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 3],
    [11, 1, 0, 0, 0, 2, 0, 4, 0],
    [0, 0, 0, 0, 17, 0, 9, 0, 14],
    [0, 0, 0, 17, 0, 5, 0, 13, 0],
    [7, 0, 2, 0, 5, 0, 0, 0, 10],
    [0, 1, 0, 9, 0, 0, 0, 0, 0],
    [4, 0, 4, 0, 13, 0, 0, 0, 0],
    [0, 3, 0, 14, 0, 10, 0, 0, 0]
]

graph = Graph(matrix_of_neighbors)
optional_blocked_list = [5]
current_node = 0
goal = 8
game = Game(graph,current_node,goal,optional_blocked_list)
# graph.Dijkstra(0, optional_blocked_list)
game.play()