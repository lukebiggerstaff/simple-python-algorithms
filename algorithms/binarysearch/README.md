# Python of Binary Search [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.binarysearch.test_binarysearch -vvv
flake8 ./algorithms/binarysearch
```

## Usage
binary_search and recursive_binary_search takes a sorted list with a key and will return True if the key is in the list and False if not

## Time Complexity
Algorithm takes O(logn) time to find the key and O(1) additional space
