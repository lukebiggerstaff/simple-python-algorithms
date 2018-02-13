'''
python depth first search
'''


def depth_first_search(adj_list, visited=set(), current=None):
    if current is None:
        current = 1
    visited.add(current)
    if current in adj_list:
        for node in adj_list[current]:
            if node not in visited:
                visited.add(node)
                depth_first_search(adj_list, visited, current=node)
    return visited
