'''
python implementation of breadth first search, returns visited set
'''

from collections import deque


def breadth_first_search(adj_list, entry_node=None):
    if entry_node is None:
        entry_node = 1
    visited = set()
    queue = deque()
    queue.append(entry_node)
    while queue:
        current = queue.popleft()
        if current in adj_list:
            for node in adj_list[current]:
                if node not in visited:
                    queue.append(node)
        visited.add(current)
    return visited


def recursive_bfs(adj_list, visited=set(), current=None):
    if current is None:
        current = 1
    visited.add(current)
    if current in adj_list:
        for node in adj_list[current]:
            if node not in visited:
                visited.add(node)
                recursive_bfs(adj_list, visited, current=node)
    return visited
