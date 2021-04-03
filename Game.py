from Graph import Graph
import numpy as np
class Game():
    def __init__(self,graph,starting_node,end_node = 8,blocked_nodes = list()):
        self.current_node = starting_node
        self.goal = end_node
        self.graph = graph
        self.blocked_nodes = blocked_nodes
    def play(self):
        path = [self.current_node]
        total_cost = 0
        if(self.current_node!=self.goal):
            while(self.current_node != self.goal):
                self.blocked_nodes = self.get_random_blocked_lists(self.graph.vertices,self.goal)
                minimum_table = self.graph.Dijkstra(self.current_node,self.blocked_nodes)
                if(minimum_table[self.goal][1] == None):
                    print("There is no way, choose random neighbor")
                    print("Game Over! cannot move")
                    break
                else:
                    print("there is a way to the goal, choosing the best node to get there")
                    node = self.goal
                    path_nodes = []
                    while(node != self.current_node):
                        path_nodes.append(node)
                        node = minimum_table[node][1]

                        print("------------")
                path_nodes = path_nodes[::-1]
                print("the path: ",path_nodes)
                print("the cost to move from {} to {} is {}".format(self.current_node,path_nodes[0],self.graph.graph[self.current_node][path_nodes[0]]))
                total_cost += self.graph.graph[self.current_node][path_nodes[0]]
                self.current_node = path_nodes[0]
                path.append(self.current_node)
                if(self.current_node == self.goal):
                    print("got to the goal with cost: ",total_cost)
                    print("The path was: ",path)

    def get_random_blocked_lists(self, vertices, goal):
        import random
        blocked_list = []
        list_of_vertices = [i for i in range(vertices)]
        blocked_list.append(random.choice(list_of_vertices))
        blocked_list.append(random.choice(list_of_vertices))
        blocked_list.append(random.choice(list_of_vertices))
        blocked_list = list(set(blocked_list))
        if(goal in blocked_list):
            blocked_list.remove(goal)
        if(self.current_node in blocked_list):
            blocked_list.remove(self.current_node)
        print(random.choice(list_of_vertices))
        return blocked_list