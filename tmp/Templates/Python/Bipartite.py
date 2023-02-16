class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for person, disliked in dislikes:
            adj[person].append(disliked)
            adj[disliked].append(person)
            
        
        colors = {}
        
        for person in range(1,n):
            if person not in colors:
                colors[person] = 0
                stack = [person]
                 
                while stack:
                    curr = stack.pop()
                    
                    for nei in adj[curr]:
                        if nei not in colors:
                            colors[nei] = colors[curr] ^ 1
                            stack.append(nei)
                            
                        elif colors[nei] == colors[curr]:
                            return False
        return True