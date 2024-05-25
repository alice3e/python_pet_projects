import networkx as nx
import matplotlib.pyplot as plt
from numpy import inf

class Graph_exception(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "unknown error"

    def __str__(self):
        return self.message
    
    

class Graph:
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
        self._type_direction = "unoriented"
        self._type_weight = "unweighted"
        self._adjacency_dict = self._convert_to_dict(adj_lst) if adj_lst is not None else {}
        self._adjacency_mtx = adj_mtx if adj_mtx is not None else self.adj_lst_to_adj_mtx()
        self._incidence_mtx = inc_mtx if inc_mtx is not None else [[]]

        
    def __str__(self):
        """Returns a string representation of the adjacency matrix."""
        return "\n".join([" ".join(str(cell) for cell in row) 
                         for row in self.adj_lst_to_adj_mtx()])

    def _convert_to_dict(self, adj_lst):
        """Converts an adjacency list to an adjacency dictionary."""
        adj_dict = {}
        for i, neighbors in enumerate(adj_lst):
            adj_dict[i] = neighbors 
        return adj_dict
    
    def adj_mtx_to_adj_lst(self):
        """Converts the adjacency matrix to an adjacency list."""
        num_vertices = len(self._adjacency_mtx) 
        adj_list = [[] for _ in range(num_vertices)] 

        for i in range(num_vertices):
            for j in range(num_vertices):
                if self._adjacency_mtx[i][j] == 1:  # Assuming unweighted graph (1 for edge)
                    adj_list[i].append(j)
        return adj_list
        
    def adj_lst_to_adj_mtx(self):
            """Converts the adjacency dictionary to an adjacency matrix."""

            # Find the maximum vertex number to determine the matrix size
            # Find the maximum vertex number to determine the matrix size
            max_vertex = 0
            for vertex, neighbors in self._adjacency_dict.items():
                max_vertex = max(max_vertex, vertex, *(neighbors if neighbors else [vertex])) 

            num_vertices = max_vertex + 1  # Add 1 to account for zero-based indexing
            adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
            
            for id, edge in self._adjacency_dict.items():
                v_from, v_to = edge[0],edge[1]
                if(self._type_direction == "unoriented"):
                    adj_matrix[v_from][v_to] = 1
                    adj_matrix[v_to][v_from] = 1
                else:
                    adj_matrix[v_from][v_to] = 1

            return adj_matrix
    
    def test_error(self):
        raise Graph_exception("test error")
    
    def plot_graph(self):
        """Plots the graph using networkx and matplotlib."""
        adj_matrix = self.adj_lst_to_adj_mtx()  # Get the adjacency matrix
        num_vertices = len(adj_matrix)

        graph = nx.Graph()  # Create a NetworkX graph object (or nx.DiGraph)

        # Add edges based on the adjacency matrix
        for i in range(num_vertices):
            for j in range(num_vertices):
                if adj_matrix[i][j] != 0:  # An edge exists
                    if self._type_weight == "unweighted":
                        graph.add_edge(i, j)
                    else:
                        weight = adj_matrix[i][j] 
                        graph.add_edge(i, j, weight=weight)

        # Set layout for the graph (adjust as needed)
        if self._type_direction == "unoriented":
            pos = nx.spring_layout(graph) # Spring layout for unoriented graphs
            #print("spring layout")
        else:
            pos = nx.shell_layout(graph)  # Shell layout for oriented graphs 
            #print("shell layout")

        # Draw the graph
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")

        # Draw edge labels (for weighted graphs)
        if self._type_weight == "weighted":
            labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

        plt.title("Graph Visualization")
        plt.show()
        
    def get_neighbors(self, vertex_ind):
        neighbors_list = []
        if self._adjacency_mtx != []:
            if(vertex_ind >= len(self._adjacency_mtx)): raise Graph_exception("vertex index error")
            for i in range(len(self._adjacency_mtx)):
                if self._adjacency_mtx[vertex_ind][i] != 0:
                    neighbors_list.append(i)
        return neighbors_list
        
    def bfs_shortest_unoriented_path(self,start_ind, end_ind) -> int:
        if self._type_direction == "oriented": raise Graph_exception
        
        queue = []
        visited = {i:inf for i in range(len(self._adjacency_mtx))}
        
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
    
    def dfs_shortest_unoriented_path(self,start_ind, end_ind) -> int:
