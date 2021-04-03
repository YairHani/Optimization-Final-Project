import sys
import numpy as np
import collections
class Graph:

    def __init__(self,matrix_of_neighbors):
        self.vertices = len(matrix_of_neighbors[0])
        self.graph = matrix_of_neighbors

    def print_graph(self):
        for row in range(self.vertices):
            for col in range(self.vertices):
                if(self.graph[row][col] != 0):
                    print("vertex: ",row, " to ",col," cost:",self.graph[row][col])
        print("The Vertices: ",self.vertices)

    def next_node_in_graph(self, table, closed_list, open_list):
        global return_key

        flag = 0
        for key in table.keys():
            if(key in open_list and flag == 0):
                return_key = key
                flag = 1
            else:
                if(key in open_list):
                    if(table[key][0] < table[return_key][0]):
                        return_key = key
        print("the return key is: ",return_key)
        return return_key

    def Dijkstra(self, S, blocked_nodes =[]):
        # S is the starting vertex.

        # done:
        # 2. create a closed list of vertices that I already visited
        # 3. create an open list that I need to visit in the iteration
        # 4. check what is the maximum value for the beginning of the iteration
        # 1.1 create a minimum table
        # 1.2 in order that will be updated in each iteration
    
        open_list = [i for i in range(self.vertices)]
        closed_list = []

        print(closed_list)
        # dictionary = neighbor vertex : {distance,father of this vertex}
        max_value = sys.maxsize
        minimum_table = {}
        for vertex in range(self.vertices):
            # if(vertex not in blocked_nodes):
            if(vertex == S):
                minimum_table[vertex] = [0,None]
            else:
                minimum_table[vertex] = [max_value,None]
        print(minimum_table)

        # minimum_table = sorted(minimum_table,key=lambda x: (x[-1]))

        print(minimum_table[0])

        flag = 0
        current_vertex = S
        while(len(open_list) != 0):

            closed_list.append(current_vertex)
            open_list.remove(current_vertex)

            for neighbor_vertex in range(self.vertices):
                if(self.graph[current_vertex][neighbor_vertex] != 0 and neighbor_vertex not in blocked_nodes):
                    if(self.graph[current_vertex][neighbor_vertex] + minimum_table[current_vertex][0] <
                            minimum_table[neighbor_vertex][0]):
                        father_vertex = minimum_table[current_vertex][1]
                        if(father_vertex == current_vertex):
                            minimum_table[neighbor_vertex][0] = self.graph[current_vertex][neighbor_vertex]
                        else:
                            minimum_table[neighbor_vertex][0] = self.graph[current_vertex][neighbor_vertex] + \
                                                                minimum_table[current_vertex][0]
                        minimum_table[neighbor_vertex][1] = current_vertex

            # choosing the next
            current_vertex = self.next_node_in_graph(minimum_table, closed_list, open_list)
        print("This is S: ",S)
        print("This is the blocked nodes: ",blocked_nodes)
        print(minimum_table)
        return minimum_table
