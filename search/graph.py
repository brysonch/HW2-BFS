import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # Throw error if graph is empty or no start node is provided
        if start == None or not self.graph: raise Exception("Graph is empty")

        # Throw error if start is not in the graph
        if start not in self.graph: raise Exception("Start node "+ start +" not found in graph")

        # If graph has one node, return that node
        if start == end: return start

        # Initialize queue and visited lists, then append the first node to the queue
        # Initialize the shortest path dict: each key is a node in the graph, and its value is a list of predecessor nodes it took to get to that node
        Q = []
        visited = []
        Q.append(start)
        sp = {}
        sp[start] = []

        # While the queue is not empty, visit the node that was inserted first
        while Q:
            v = Q.pop()
            visited.append(v)

            # Find all neighbors of the visited node
            neighbors = [n for n in self.graph[v]]

            # Return the shortest path if there was an end node provided, and the visited node is the end node
            if end and v == end: return sp[v]

            # Check all the neighbors and see which ones have not been visited, then append those to the visited list and the queue
            # The value for that neighbor node key in the shortest path dict is updated to include the node's predecessors, as well as the neighbor itself
            for w in neighbors:
                if w not in visited: 
                    visited.append(w)
                    Q.append(w)
                    sp[w] = sp[v] + [w]
                
        # If no shortest path was found from start to end nodes, just return the full traversal from the start node
        if not end: return visited

        return None




