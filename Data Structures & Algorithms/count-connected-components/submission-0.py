class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        dfs on each node in range n. when one graph visited increment result. 
        '''

        adjList = {i : [] for i in range(n)}
        res = 0
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)
            return True
        
        for i in range(n):
            if dfs(i):
                res += 1
        return res