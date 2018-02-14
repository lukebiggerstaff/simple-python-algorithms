# Python 0/1 Knapsack Algorithm [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-algorithms)

## Layout
folder consists of README, a test file and the implementation

## Testing
> from within the root directory run the following command
```sh
python -m unittest algorithms.knapsack.test_knapsack -vvv
flake8 ./algorithms/knapsack
```

## Usage
Knapsack algorithm is for finding the highest value of items that will fit within a block limited on weighting. 0/1 refers to only being able to take the whole item and not pieces of the item. the weight must be an integer or you will will quickly run into time or space complexity issues

## Time Complexity
O(nW) where n is the amount of items and W is the total weight the knapsack can hold. Dynamic Programming solution also takes O(nW) additional space in order to complete. At larger values of W you will need to optimize the space complexity by only storing the last row and not the whole table. At this point you are unable to determine which items comprise the knapsack just the optimal value.
