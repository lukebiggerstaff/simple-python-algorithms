# Python Dijkstra Implementation [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.dijkstra.test_dijkstra -vvv
flake8 ./algorithms/dijkstra
```

## Usage
Dijkstra's algorithm is a greedy algorithm that works for graphs with non-negative edge lengths. It will find the shortest or least costly path from one node to another if it exists from within the graph. If edges are not weighted then there is no need for dijkstra and you can just use breadth first search

## Time Complexity
Dijkstra's algorithm takes 
