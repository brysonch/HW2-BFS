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

        if start == None or not self.graph: raise Exception("Graph is empty")

        if start not in self.graph: raise Exception("Start node "+ start +" not found in graph")

        if start == end: return start

        Q = []
        visited = []
        Q.append(start)
        sp = {}
        sp[start] = []

        while Q:
            v = Q.pop()
            visited.append(v)
            neighbors = [n for n in self.graph[v]]
            if end and v == end: return sp[v]
            for w in neighbors:
                if w not in visited: 
                    visited.append(w)
                    Q.append(w)
                    sp[w] = sp[v] + [w]
                

        if not end: return visited

        return None




