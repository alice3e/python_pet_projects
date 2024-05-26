from graph_class import Graph
from additional_functions import generate_random_graph


if __name__ == "__main__":
    
    b = generate_random_graph(num_vertices=9, edge_chance=0.15, directed=False, weighted=True)    
    k = b.dijkstra_shortest_oriented_path(7)
    b.plot_graph()
    print(k)
    
    
