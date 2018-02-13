# Python Breadth First Search [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.breadthfirst.test_breadthfirst -vvv
flake8 ./algorithms/breadthfirst
```

## Usage
BFS takes a graph in the form of an adjacency list and visits every node in the graph by visiting every node of every node until all have been visited

## Time Complexity
BFS takes O(V + E) where V is the number of nodes and E is the number of edges between the nodes
