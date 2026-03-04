
"""
1) Levenshtein distance
Levenshtein Distance is a string metric used to measure the difference between two sequences.
It represents the minimum number of single-character edits (insertions, deletions,
 or substitutions) required to change one word into the other.

The algorithm uses Dynamic Programming to find the optimal solution by breaking the
problem down into sub-problems, typically represented in
a (m+1)*(n+1) matrix.
- Insertion: Adding a character (cost = 1).
- Deletion: Removing a character (cost = 1).
- Substitution: Replacing one character with another (cost = 1, or 0 if characters match).

Distance is minimum total cost over all sequences of edits transforming source to target.
Complexity and memory is O(mn) since we have to fill and keep (m+1)*(n+1) table.
"""

def levenshtein_distance_optimized(source: str, target: str) -> int:
    # ensure target is the shorter one to reduce memory
    if len(target) > len(source):
        source, target = target, source
    m, n = len(source), len(target)
    prev = list(range(n+1))  # D[0][j]
    for i in range(1, m+1):
        curr = [i] + [0]*n
        for j in range(1, n+1):
            curr[j] = min(
                prev[j] + 1,                   # delete
                curr[j-1] + 1,                 # insert
                prev[j-1] + (0 if source[i-1] == target[j-1] else 1)  # sub/match
            )
        prev = curr
    return prev[n]

levenshtein_distance_optimized("kitten", "sitting")

"""
2) Weighted Edit Distance
Weighted Edit Distance generalizes the Levenshtein distance by allowing different 
costs for insertion, deletion, and substitution. This is particularly useful in 
NLP for tasks like spellchecking, where substituting "a" for "s" 
(neighboring keys) might be assigned a lower cost than substituting "a" for "p".

Key concepts:
- Custom Costs: Instead of a flat cost of 1, costs can be functions of the characters involved.
- Physical Distance: In keyboard-aware models, the sub_cost_fn often utilizes Euclidean distance between key coordinates.
- Initialization: The first row and column are no longer simple sequences of integers; they are cumulative sums 
of ins_cost and del_cost.
"""
def min_edit_distance(
    source: str,
    target: str,
    ins_cost: float = 1.0,
    del_cost: float = 1.0,
    sub_cost_fn: Optional[Callable[[str, str], float]] = None
):
    '''
    sub_cost_fn(a,b) returns cost of substituting a->b, and should return 0 when a==b.
    If not provided, uses standard cost 0 if match else 1.
    '''
    if sub_cost_fn is None:
        sub_cost_fn = lambda a, b: 0.0 if a == b else 1.0

    m, n = len(source), len(target)
    D = [[0.0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        D[i][0] = D[i-1][0] + del_cost
    for j in range(1, n+1):
        D[0][j] = D[0][j-1] + ins_cost

    for i in range(1, m+1):
        for j in range(1, n+1):
            D[i][j] = min(
                D[i-1][j] + del_cost,
                D[i][j-1] + ins_cost,
                D[i-1][j-1] + sub_cost_fn(source[i-1], target[j-1]),
            )
    return D, D[m][n]

# Example: make substitutions more expensive than insert/delete
D2, dist2 = min_edit_distance(
    "intention", "execution",
    ins_cost=1.0, del_cost=1.0,
    sub_cost_fn=lambda a, b: 0.0 if a == b else 2.0
)