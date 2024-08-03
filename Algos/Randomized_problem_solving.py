"""  Randomized QuickSort:

Problem: Sorting a list of elements efficiently.
Description: QuickSort is a commonly used sorting algorithm, and a randomized version can be even more efficient in practice. The randomized algorithm randomly selects a pivot element, which helps avoid worst-case scenarios.
Python Implementation:
 """
import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + equal + randomized_quick_sort(right)

# Example usage:
unsorted_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = randomized_quick_sort(unsorted_list)
print(sorted_list)

""" 2. Randomized Prim's Algorithm:

Problem: Finding the minimum spanning tree (MST) of a weighted, connected graph.
Description: Prim's algorithm usually starts with an arbitrary vertex, but the randomized version starts with a random vertex, which can lead to different MSTs. Randomization can be useful in load balancing or network design problems.
Python Implementation:
 """
import random

def randomized_prims(graph):
    start_vertex = random.choice(list(graph.keys()))
    mst = set()
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex]]
    while edges:
        cost, u, v = min(edges)
        if v not in mst:
            mst.add(v)
            edges.extend((c, v, neighbor) for neighbor, c in graph[v] if neighbor not in mst)
        edges.remove((cost, u, v))
    return mst

# Example usage:
weighted_graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 5)],
    'D': [('B', 1), ('C', 5)],
}
minimum_spanning_tree = randomized_prims(weighted_graph)
print(minimum_spanning_tree)

""" 3. Randomized Rabin-Karp Algorithm:

Problem: Finding occurrences of a substring within a longer string (string matching).
Description: The Rabin-Karp algorithm uses a rolling hash function to compare substrings efficiently. Randomization can be applied in choosing the hash function, making it less susceptible to specific input patterns.
Python Implementation:

 """
import random
import hashlib

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hashlib.md5(pattern.encode()).hexdigest()
    results = []
    for i in range(n - m + 1):
        subtext = text[i:i + m]
        subtext_hash = hashlib.md5(subtext.encode()).hexdigest()
        if subtext_hash == pattern_hash:
            if subtext == pattern:
                results.append(i)
    return results

# Example usage:
text = "ABABCABABABABCABABCAB"
pattern = "ABAB"
matches = rabin_karp(text, pattern)
print(matches)