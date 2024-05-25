from test_class import Graph
import networkx as nx
import matplotlib.pyplot as plt
import random
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
    graph = nx.Graph() if not directed else nx.DiGraph()
    for i in range(num_vertices):
        graph.add_node(i)

    for i in range(num_vertices):
        for j in range(i + 1 if not directed else num_vertices):
            if i != j and random.random() < edge_chance:
                if weighted:
                    weight = random.randint(1, 10)  # Adjust weight range as needed
                    graph.add_edge(i, j, weight=weight)
                else:
                    graph.add_edge(i, j)

    # Convert to your Graph class
    adj_dict = {node: list(graph.neighbors(node)) for node in graph.nodes()}
    my_graph = Graph(adj_lst=list(adj_dict.values()))
    my_graph._type_direction = "oriented" if directed else "unoriented"
    my_graph._type_weight = "weighted" if weighted else "unweighted"

    return my_graph



if __name__ == "__main__":
    
    # a = Graph(adj_lst=[
    #     [0,1],
    #     [1,2],
    #     [3,4],
    #     [4,1],
    #     [4,2],
    #     [4,3],
    # ])
    
    b = generate_random_graph(10, 0.5, directed=True, weighted=False)
    print(b)
    b.plot_graph()

    
    