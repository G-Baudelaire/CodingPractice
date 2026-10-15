from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections = set(tuple(connection) for connection in connections)
        children = [[] for _ in range(n)]
        for node1, node2 in connections:
            children[node1].append(node2)
            children[node2].append(node1)

        seen = set()
        new_connections = set()
        def dfs(node, parent):
            seen.add(node)
            if parent is not None:
                new_connections.add((node, parent))

            for child in children[node]:
                if child in seen:
                    continue
                dfs(child, node)

        dfs(0, None)

        return len(new_connections.difference(connections))
