def rdfs(graph, node, visited, stack):
    visited.add(node)
    if node in graph:
        for edge in graph[node]:
            if edge not in visited:
                rdfs(graph, edge, visited, stack)
    stack.append(node)


def topological_sort(graph):
    """
    takes a directed acyclic graph and
    returns the topologically sorted order
    """

    stack = list()
    visited = set()
    unvisited = set(
        [e for e in graph]).union(
        [v for e in graph for v in graph[e]]
    )
    for node in unvisited:
        if node not in visited:
            rdfs(graph, node, visited, stack)
    return stack
