from graph_class import Graph
from additional_functions import generate_random_graph


if __name__ == "__main__":
    
    b = generate_random_graph(8, 0.15, directed=True, weighted=True)    
    b.plot_graph()
    #b.dijkstra_shortest_oriented_path()
    
    
