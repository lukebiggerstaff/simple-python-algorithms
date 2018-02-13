# Python Depth First Search [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.depthfirst.test_depthfirst -vvv
flake8 ./algorithms/depthfirst
```

## Usage
Depth first search takes an adjacency list and will visit every node in the graph if reachable.

## Time Complexity
Algorithm takes O(V + E) time to visit all nodes, where V are the nodes in the graph and E are the edges between them and O(V) additional space as it stores which nodes have been visited previously
