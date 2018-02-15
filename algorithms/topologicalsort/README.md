# Python Topological Sort [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.topologicalsort.test_topologicalsort -vvv
flake8 ./algorithms/topologicalsort
```

## Usage
When used on a directed acyclic graph, topological sort will return all u -> v such that no v comes before u. This means that any node that comes before another node will be returned in the proper order.

## Time Complexity
O(V + E) in time O(V) for space where V is every vertex in the graph and E is every edge in the graph.
