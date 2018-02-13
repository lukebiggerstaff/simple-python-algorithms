# Python Merge Sort [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.mergesort.test_mergesort -vvv
flake8 ./algorithms/mergesort
```

## Usage
Merge Sort recursively breaks up an unsorted list and then merges them back togetheir proper order. 

## Time Complexity
Time complexity is O(nlog(n)) and Space Complexity is O(n) as you end up copying over the entire list into smaller lists for sorting.
