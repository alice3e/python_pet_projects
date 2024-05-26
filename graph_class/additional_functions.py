import networkx as nx
import matplotlib.pyplot as plt
import random
from graph_class import Graph

def generate_random_graph(num_vertices, edge_chance, directed=False, weighted=False):
    """Generates a random Graph object.

    Args:
        num_vertices (int): The number of vertices in the graph.
        edge_chance (float): The probability of creating an edge between any two vertices.
        directed (bool, optional): Whether the graph should be directed. Defaults to False.
        weighted (bool, optional): Whether the graph should be weighted. Defaults to False.

    Returns:
        Graph: A randomly generated Graph object.
    """
    seed = 21
    random.seed(seed)
    graph = nx.Graph() if not directed else nx.DiGraph()
    for i in range(num_vertices):
        graph.add_node(i)

    for i in range(num_vertices):
        for j in range(i + 1 if not directed else num_vertices):
            if i != j and random.random() < edge_chance:
                if weighted:
                    weight = random.randint(1, 9)  # Adjust weight range as needed
                    graph.add_edge(i, j, weight=weight)
                else:
                    graph.add_edge(i, j)

    # Convert to adjacency matrix
    adj_mtx = [[0] * num_vertices for _ in range(num_vertices)]
    for i, j in graph.edges():
        if weighted:
            adj_mtx[i][j] = graph.edges[i, j]['weight']
        else:
            adj_mtx[i][j] = 1
        if not directed:
            if weighted:
                adj_mtx[j][i] = graph.edges[i, j]['weight']
            else:
                adj_mtx[j][i] = 1
    
    my_graph = Graph(adj_mtx=adj_mtx)
    my_graph._Graph__type_direction = "oriented" if directed else "unoriented"
    my_graph._Graph__type_weight = "weighted" if weighted else "unweighted"

    return my_graph