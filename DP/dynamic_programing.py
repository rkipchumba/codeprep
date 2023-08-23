'''Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.'''


def min_coins(coins, S):
    N = len(coins)
    # Create a 2D DP table where dp[i][j] represents the minimum coins needed to make sum j using the first i coins.
    dp = [[0] * (S + 1) for _ in range(N + 1)]

    # Initialize the first column with zeros (you need zero coins to make a sum of zero).
    # Initialize the first row with a large value (larger than the maximum possible number of coins).
    for j in range(1, S + 1):
        dp[0][j] = float('inf')

    # Dynamic Programming loop
    for i in range(1, N + 1):
        for j in range(1, S + 1):
            if coins[i - 1] > j:
                # If the current coin's value is greater than the current sum, copy the value from the row above.
                dp[i][j] = dp[i - 1][j]
            else:
                # Choose the minimum between the value from the row above and the value from the same row
                # but shifted by the coin's value plus 1 (since we're using one more coin).
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

    if dp[N][S] == float('inf'):
        # If it's still infinity, it's not possible to form the sum S.
        return "Not possible"
    return dp[N][S]


# Example usage
coins = [3, 5, 11]
S = 11
result = min_coins(coins, S)
print("Minimum number of coins:", result)
