class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        output = []
        cycle = set()
        visit = set() 

        def dfs(crs):
            if crs in cycle: 
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
