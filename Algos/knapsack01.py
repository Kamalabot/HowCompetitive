def knapsack(values, weights, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i, k) in lookup:
        return lookup[(i, k)]
    if i == len(values):
        return 0
    elif k < 0:
        return float('-inf')
    else:
        lookup[(i, k)] = max(values[i]+knapsack(values, weights, k-weights[i], i+1, lookup),
                             knapsack(values, weights, k, i+1))
        return lookup[(i, k)]