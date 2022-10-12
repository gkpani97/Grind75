#dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # defaultdict([]) is expected to return an empty list by 'default' if the key is not present in the dict.
        graph = collections.defaultdict(list)
        
        # adding the vertices any vertex is connected to, as its neighbour to define the graph.
        for start, end in prerequisites:
            graph[start].append(end)
        # creating a register of vertices with following denominations:
        #  0: if it is not yet visited
        # -1: if it is being visited. it's case is still open.
        #  1: if it has been completely visited. case closed.
        visited = [0] * numCourses
        
        #dfs function
        def dfs(v):
            # return False if it is being visited, as that wld mean, this vertex is a part of a cycle
            if visited[v] == -1: return False
            
            # return True if it has been visited. If it has been been visited, there is bound to be no cycle ahead, as it it wld have been detected otherwise.
            if visited[v] == 1: return True
            
            # now otherwise we set visited[i] as -1 and do dfs on all its neighbour, so that if there is any link ending up at 'i', we wld get False, and discover the chain.
            visited[v] = -1
            
            for node in graph[v]:
                if not dfs(node):
                    return False
            
            visited[v] = 1
            # as the above loop at this point ran without returning False we can return True now, as i isnt part of any cycle
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                # Likewise if here any node returns False, it is part of a cycle so we close the code, and go home after returning False
                return False
            
        return True
