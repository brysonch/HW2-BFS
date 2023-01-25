# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Assignment Tasks

## Testing BFS Functions (Bryson Choy)
graph.py defines a class called Graph with a class method called bfs, which takes in a start and optional end node. If only a start node is provided, BFS traversal is computed and returned to the user. If a start and end node are both provided, the shortest path via BFS is returned to the user. Empty graphs, omission of a start node, and unconnected graphs are handled by error messages and test via unit tests in test_bfs.py.

In test_bfs.py:
* Run test_bfs_traversal, which tests a BFS traversal on the /data/tiny_network.adjlist with the start node "Michael Keiser" to get a 59-node traversal path, ending in "Charles Chiu"
* Run test_bfs, which tests a BFS traversal on the /data/citation_network.adjlist with the start node "Michael Keiser" to get a shortest path traversal to "Nevan Krogan". Other exception cases are handled here: unconnected graph, omission of start node, empty graph, start node missing from graph, and one-node graph (start node = end node).



