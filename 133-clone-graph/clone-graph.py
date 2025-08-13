"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        head = Node(val=node.val)
        visited = {node : head}
        q = deque([node])
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(val=nei.val)
                    q.append(nei)
                visited[curr].neighbors.append(visited[nei])
        return head