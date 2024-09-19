# Problem: Climbing Stairs (LeetCode 70)
# The number of ways to reach the nth step can be solved using a dynamic programming approach,
# similar to the Fibonacci sequence, where the number of ways to reach the nth step depends
# on the number of ways to reach the (n-1)th and (n-2)th steps.

# intu 0: if only one step, there is just a single way
# intu 1: build a solution list for each num of steps
# intu 2: build the list by enumerating range 3 to n + 1


def climbing_stairs(n: int) -> int:
    if n == 1:
        return 1

    # dp[idx] reps the number of ways
    dp = [0] * (n + 1)
    # there is one way to reach 1 step,
    # there is 2 way to reach 2 steps
    dp[1], dp[2] = 1, 2

    # updating solution for each step
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climbing_stairs(5))
