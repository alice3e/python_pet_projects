import networkx as nx
import matplotlib.pyplot as plt
from numpy import inf
import heapq

class Graph_exception(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "unknown error"

    def __str__(self):
        return self.message
    
    

class Graph:
    
    __type_direction = ""
    __type_weight = ""
    __adjacency_dict = dict()
    __adjacency_mtx = [[]]
    __incidence_mtx = [[]]
    __number_of_nodes = 0
    def __init__(self, adj_mtx=None, inc_mtx=None, adj_lst=None):
        """Initializes a Graph object.

        Args:
            adj_mtx (list, optional): The adjacency matrix representation of the graph. 
                                     Defaults to None (an empty graph).
            inc_mtx (list, optional): The incidence matrix representation of the graph. 
                                     Defaults to None (an empty graph).
            adj_lst (list, optional): The adjacency list representation of the graph.
                                     Defaults to None (an empty graph).

        The graph can be initialized using any one of the following:
            - Adjacency matrix: A list of lists representing connections between vertices.
            - Incidence matrix: A list of lists representing relationships between vertices and edges.
            - Adjacency list: A list where each index represents a vertex and the corresponding 
                              element is a list of its neighbors.

        If no input is provided, an empty graph is created.
        """
       
        self.__type_direction = "unoriented"
        self.__type_weight = "unweighted"
        self.__adjacency_dict = self._convert_to_dict(adj_lst) if adj_lst is not None else {}
        self.__adjacency_mtx = adj_mtx if adj_mtx is not None else self.adj_lst_to_adj_mtx()
        self.__incidence_mtx = inc_mtx if inc_mtx is not None else [[]]
        
        
        if(len(self.__adjacency_mtx) != 0):
            self.__number_of_nodes = len(self.__adjacency_mtx)
        else:
            raise Graph_exception("number of nodes is incorrect")
        
        if(len(self.__adjacency_mtx) != 0 and self.__type_weight != "weighted"):
            self.__adjacency_dict = self.adj_mtx_to_adj_lst()

    def __str__(self):
        """Returns a string representation of the adjacency matrix."""
        matrix_str = "\n".join([" ".join(map(str, row)) for row in self.__adjacency_mtx])
        return matrix_str


    def _convert_to_dict(self, adj_lst):
        """Converts an adjacency list to an adjacency dictionary."""
        adj_dict = {}
        for i, neighbors in enumerate(adj_lst):
            adj_dict[i] = neighbors 
        return adj_dict
    
    def adj_mtx_to_adj_lst(self):
        """Converts the adjacency matrix to an adjacency dictionary."""
        if(self.__type_weight == "weighted"): raise Graph_exception("convertation from mtx to list is not supported for weighted graphs")
        num_vertices = len(self.__adjacency_mtx)
        adj_dict = {i: [] for i in range(num_vertices)}

        for i in range(num_vertices):
            for j in range(num_vertices):
                if self.__adjacency_mtx[i][j] != 0:
                    adj_dict[i].append(j)
                    
        return adj_dict
        
    def adj_lst_to_adj_mtx(self):
        if(self.__type_weight == "weighted"): raise Graph_exception("convertation from list to mtx is not supported for weighted graphs")
        """Converts the adjacency dictionary to an adjacency matrix."""

        # Find the maximum vertex number to determine the matrix size
        max_vertex = max(self.__adjacency_dict.keys(), default=0)
        for neighbors in self.__adjacency_dict.values():
            if isinstance(neighbors, list):
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        max_vertex = max(max_vertex, neighbor[0])
                    else:
                        max_vertex = max(max_vertex, neighbor)

        num_vertices = max_vertex + 1  # Add 1 to account for zero-based indexing
        adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

        for vertex, neighbors in self.__adjacency_dict.items():
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):  # For weighted edges
                    v_to, weight = neighbor
                    if self.__type_direction == "unoriented":
                        adj_matrix[vertex][v_to] = weight
                        adj_matrix[v_to][vertex] = weight
                    else:
                        adj_matrix[vertex][v_to] = weight
                else:  # For unweighted edges
                    v_to = neighbor
                    if self.__type_direction == "unoriented":
                        adj_matrix[vertex][v_to] = 1
                        adj_matrix[v_to][vertex] = 1
                    else:
                        adj_matrix[vertex][v_to] = 1

        return adj_matrix

    
    def test_error(self):
        raise Graph_exception("test error")
    
    
    def plot_graph(self):
        """Plots the graph using networkx and matplotlib."""
        if(self.__type_weight != "weighted"):
            adj_matrix = self.adj_lst_to_adj_mtx()  # Get the adjacency matrix
        else: 
            adj_matrix = self.__adjacency_mtx
        num_vertices = len(adj_matrix)

        # Create a NetworkX graph object based on the type of graph (oriented or unoriented)
        if self.__type_direction == "unoriented":
            graph = nx.Graph()
        else:
            graph = nx.DiGraph()

        # Add edges based on the adjacency matrix
        for i in range(num_vertices):
            for j in range(num_vertices):
                if adj_matrix[i][j] != 0:  # An edge exists
                    if self.__type_weight == "unweighted":
                        graph.add_edge(i, j)
                    else:
                        weight = adj_matrix[i][j]
                        graph.add_edge(i, j, weight=weight)

        # Set layout for the graph
        if self.__type_direction == "unoriented":
            pos = nx.spring_layout(graph)  # Spring layout for unoriented graphs
        else:
            pos = nx.shell_layout(graph)  # Shell layout for oriented graphs

        # Draw the graph
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")

        # Draw edge labels to show weights if the graph is weighted
        if self.__type_weight == "weighted":
            labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

        plt.title("Graph Visualization")
        plt.show()

    def get_neighbors(self, vertex_ind):
        neighbors_list = []
        if self.__adjacency_mtx != []:
            if(vertex_ind >= len(self.__adjacency_mtx)): raise Graph_exception("vertex index error")
            for i in range(len(self.__adjacency_mtx)):
                if self.__adjacency_mtx[vertex_ind][i] != 0:
                    neighbors_list.append(i)
        return neighbors_list
    
    def get_distance_between_nodes(self, start_ind, end_ind):
        if(len(self.__adjacency_mtx) != 0 ):
            return self.__adjacency_mtx[start_ind][end_ind]
        else:
            raise Graph_exception("get_distance_between_nodes not fully implemented")
        
    def bfs_shortest_unoriented_path(self,start_ind, end_ind) -> int:
        print(f'a = {self.a}')
        if self.__type_direction == "oriented": raise Graph_exception
        
        queue = []
        visited = {i:inf for i in range(len(self.__adjacency_mtx))}
        
        visited[start_ind] = 0
        queue.append(start_ind)
        
        while queue:
            node = queue.pop(0)
            if(node == end_ind):
                return visited[node]
            for i in self.get_neighbors(node): 
                if  visited[i] == inf: 
                    queue.append(i)
                    visited[i] = visited[node] + 1
        return -1
    
    def dijkstra_shortest_oriented_path(self,start_ind) -> list:
        """Dijkstra's algorithm

        Args:
            start_ind (_type_): node from where to start
        Returns:
            list: distance to all nodes
        """
        shortest_path = [inf for i in range(self.__number_of_nodes)]
        is_shortest = set()
        queue = []
        heapq.heapify(queue)
        
        
        shortest_path[start_ind] = 0
        is_shortest.add(start_ind)
        for node_id in self.get_neighbors(start_ind):
            dist = self.get_distance_between_nodes(start_ind,node_id)
            heapq.heappush(queue, (dist,node_id)   )
        
        while queue:
            print(queue)
            
    
    