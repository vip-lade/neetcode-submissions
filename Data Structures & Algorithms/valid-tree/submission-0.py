class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set() 

        def dfs(node, par):
            if node in visited: 
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue 
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
