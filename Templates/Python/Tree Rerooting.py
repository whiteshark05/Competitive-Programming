"""
https://www.codespeedy.com/tree-rerooting-technique-in-c/
"""






#https://leetcode.com/problems/count-number-of-possible-root-nodes/discuss/3256072/short-python-template-for-tree-based-dp-problems
"""
For tree-based dp problems that give you edges as inputs, below is the template

store edges into an adjancent list

define a dfs function with two key parameters (cur, prev) to control the direction we will move along an edge between cur and prev

within dfs(cur,prev), the recursion is to call t(nxt,cur) for nxt in adj[cur]-{prev}

we add memorization (@cache) so that each edge between cur and prev will only be visited twice: one from cur to prev, one from prev to cur

we call dfs(i,-1) for i in range(n). -1 denotes no prev for i, so i is the root.

Using this template, we can solve all the following problems with minor edits.
https://leetcode.com/problems/sum-of-distances-in-tree/


https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/discuss/3052569/template-for-tree-based-dp-problems-with-edges-inputs

https://leetcode.com/discuss/interview-question/2751188/Lucid-OA-new-grad-SWE

https://leetcode.com/discuss/interview-question/1463104/Media.net-or-OA-or-Minimum-cost-to-buy-oranges

https://leetcode.com/discuss/interview-question/2639890/Media.Net(Directi)-OA-On-campus-Questions-%3A)

https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

https://leetcode.com/discuss/interview-question/2788156/OA-2022-or-Pythagorean-Triplets
"""
adj, g =defaultdict(set), Counter(map(tuple,guesses))
for i,j in edges:
    adj[i].add(j)
    adj[j].add(i)
        
@cache
def t(cur,prev):
    return g[prev,cur]+sum(t(kid,cur) for kid in adj[cur]-{prev})

return sum(t(i,-1)>=k for i in adj)


#https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/discuss/3052596/Re-rooting-or-O(N)-or-Explained
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        subtree_sum = [0] * n
        self.max_cost = 0

        def dfs(i, parent):
            max_nei_sum = 0
            for nei in adj[i]:
                if nei == parent: continue
                max_nei_sum = max(max_nei_sum, dfs(nei, i))
            subtree_sum[i] = max_nei_sum + price[i]
            return subtree_sum[i]

        def reroot(i, parent, parent_contribution):
            # nodes with the top two maximum subtree_sum
            max_i_1, max_i_2 = -1, -1
            max_subtree_sum_1, max_subtree_sum_2 = 0, 0
            for nei in adj[i]:
                if nei == parent: continue 
                if subtree_sum[nei] > max_subtree_sum_2:
                    max_subtree_sum_2 = subtree_sum[nei]
                    max_i_2 = nei
                if max_subtree_sum_2 > max_subtree_sum_1:
                    max_subtree_sum_1, max_subtree_sum_2 = max_subtree_sum_2, max_subtree_sum_1
                    max_i_1, max_i_2 = max_i_2, max_i_1
            self.max_cost = max(self.max_cost, parent_contribution, max_subtree_sum_1)
            for nei in adj[i]:
                if nei == parent: continue
                if nei == max_i_1:
                    reroot(nei, i, price[i] + max(max_subtree_sum_2, parent_contribution)) 
                else:
                    reroot(nei, i, price[i] + max(max_subtree_sum_1, parent_contribution))
        dfs(0, -1)
        reroot(0, -1, 0)
        return self.max_cost
    
def dfs()