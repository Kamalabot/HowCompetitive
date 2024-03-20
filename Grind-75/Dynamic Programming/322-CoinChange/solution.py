from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Returns how many coins are needed, not the denomination
        coins_need = [float("inf") for _ in range(amount + 1)]
        # initialize the list with elements bigger than required amt
        coins_need[0] = 0  # make the 0th element as 0, as no coins is required for 0 amnt
        for i in range(1, amount + 1):  # enumerate over the range 1 to amt + 1
            # if i % 5 == 0:
                # print(i)
            for coin in coins:  # enumerate the coins given
                # print(coin)
                if coin <= i:  # every i in the amount loop check if coin lte i
                    coins_need[i] = min(coins_need[i], coins_need[i-coin]+1)
                    # to find the reason for above step, come up the best solution
                    # by brute force, or by solving for some examples
#            print(f'coins needed array: {coins_need}')

        return coins_need[-1] if coins_need[-1] != float("inf") else -1


rsn = Solution()
# coins = [1, 2, 5]
# amt = 11
coins = [2, 5, 10, 20, 100, 500]
amt = 551
amt1 = 752

print(rsn.coinChange(coins, amt))
print(rsn.coinChange(coins, amt1))


"""
Brute Force Trials:
    > Divide amount by biggest denom and get reminder
        551 % 500
    > check if reminder is bigger than next biggest denom
        > Try dividing reminder with next big denom
            51 % 100  == 51 which means
        else go to the next biggest
            51 % 20 == 11
    > goes through above step until reaching 1 or 0
        11 % 10 == 1  or 10 % 10 == 0
    > if reaching 1 then need to discard denom and
    go to next lowest
    > if reached the last denom, then need to subtract
    the last denom multiple times until reminder is 
    equal to the previous denom
"""