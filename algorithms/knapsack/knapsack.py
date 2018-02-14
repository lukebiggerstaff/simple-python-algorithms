def knapsack(items, weight):
    '''
    python implementation of knapsack
    '''

    num_items = len(items)
    # create matrix for all items plus the empty set
    # and set zero values for empty knapsack
    value_matrix = [[] for _ in range(num_items + 1)]
    for _ in range(weight + 1):
        value_matrix[0].append(0)
    for i in range(1, num_items + 1):
        item_weight = items[i-1][0]
        item_value = items[i-1][1]
        for w in range(weight + 1):
            prev_value = value_matrix[i - 1][w]
            if item_weight <= w:
                current_value = value_matrix[i-1][w-item_weight] + item_value
            else:
                current_value = 0
            max_value = max(prev_value, current_value)
            value_matrix[i].append(max_value)
    return value_matrix
