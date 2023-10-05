def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def unbounded_knapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    current_weight = 0

    for item in items:
        if current_weight + item[0] <= capacity:
            total_value += item[1]
            current_weight += item[0]
        else:
            fraction = (capacity - current_weight) / item[0]
            total_value += fraction * item[1]
            break

    return total_value
