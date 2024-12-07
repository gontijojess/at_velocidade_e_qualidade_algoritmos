import sys
sys.stdout.reconfigure(encoding='utf-8')
def knapsack_dinamic(values, weight, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weight[i - 1]]
                remove = dp[i - 1][w]
                dp[i][w] = max(include, remove)
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

values = [80, 120, 170, 150]
weight = [5, 10, 20, 30]
capacity = 55

result = knapsack_dinamic(values, weight, capacity)
print(f"O valor máximo que é possível carregar na moxila é {result}")