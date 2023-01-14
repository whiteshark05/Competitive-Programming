"""
Bellman-Ford
Time: O(VE)
Space: O(N)
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        return max(dist) if max(dist) < float("inf") else -1

"""
Dijkstra
Time: O(E+VlogV)
Space: O(V+E)
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, K)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == N else -1