'''
python implementation of breadth first search, returns visited set
'''

from collections import deque


def breadth_first_search(adj_list, entry_node=None, visited=set()):
    if entry_node is None:
        entry_node = 1
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
