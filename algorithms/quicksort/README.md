# Python Quicksort [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.quicksort.test_quicksort -vvv
flake8 ./algorithms/quicksort
```

## Usage
quicksort takes an unsorted list and will return a sorted list

## Time Complexity
Algorithm takes O(n * logn) time to sort the list in the average case with a small constant factor, in the worst case it is O(n^2) if the pivot is poorly chosen quicksort changes the list in place and takes O(1) additional space
