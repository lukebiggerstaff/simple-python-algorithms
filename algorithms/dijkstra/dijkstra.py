'''
python implementation of dijkstra's algorithm with heap data structure
'''

import heapq


class Heap(object):

    def __init__(self, heap=None):
        if heap is None:
            self.heap = []
        else:
            self.heap = heap
            try:
                heapq.heapify(self.heap)
            except TypeError as e:
                self.heap = []
                print(e)

    def add(self, edge):
        heapq.heappush(self.heap, edge)

    def extract_min(self):
        try:
            return heapq.heappop(self.heap)
        except IndexError as e:
            print('Heap is empty')

    def is_empty(self):
        return len(self.heap) == 0


def dijkstra(adj_list, start):
    distance = dict()
    s = set(
        [e for e in adj_list]).union(
        [v for e in adj_list for v in adj_list[e]]
    )
    for edge in s:
        if edge is start:
            distance[edge] = 0
        else:
            # 10 ** 20 is representative of infinity
            distance[edge] = 10 ** 20
    queue = Heap()
    visited = set()
    queue.add((0, start))
    while not queue.is_empty():
        dist, current = queue.extract_min()
        if current not in visited and current in adj_list:
            for edge, length in adj_list[current].items():
                total_distance = dist + length
                queue.add((total_distance, edge))
                if total_distance < distance[edge]:
                    distance[edge] = total_distance
            visited.add(current)
    return distance
