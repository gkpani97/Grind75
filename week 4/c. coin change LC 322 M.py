class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use dynamic prog.
        # if ammount is zero itself, zero coins will add upto the amount. so, return zero
        if not amount: return 0
        
        # dp list to store the minimum coins required for any amount below the target amount.
        dp = [0] * amount
        
        # we iterate through the dp list and find the coins required for every 
        for i in range(1, amount + 1):
            # this var records the minimum coins required if for the current target amt requires a certain coin value as the last coin to be added to the knapsack. so the if [1 , 2, 5] are coins, this var keeps the minimum coins to reach the target if we chose 1 or 2 or 5 unit coin respectively
            minimum_coins = math.inf
            
            for coin_value in coins:
                #  if coin_ value = target, then one coin is required
                if i - coin_value == 0:
                    minimum_coins = 1
                # else we iterate through the other coins to check if a minimum count is possible by taking the min()
                elif i - coin_value > 0:
                    # we check if target - coin value is a valid combination. We progress if it is.
                    if dp[i - coin_value - 1] != -1:
                        minimum_coins = min(minimum_coins, 1 + dp[i - coin_value - 1])

            # now if the minimum coins is no infinity, target amount is a valid combination and we add the coin count to dp list, else it is invalid, and we add -1            
            if minimum_coins == math.inf:
                dp[i - 1] = -1
            else:
                dp[i - 1] = minimum_coins
            
        return dp[-1]
