def solve():
    X = input().strip()
    Y = input().strip()
    S, R = map(int, input().split())
    
    n = len(X)
    m = len(Y)
    
    # Reverse of Y
    Y_rev = Y[::-1]
    
    # dp[i] = (min_substrings, min_factor) to form X[0:i]
    # Initialize with impossible values
    INF = float('inf')
    dp = [(INF, INF)] * (n + 1)
    dp[0] = (0, 0)  # Empty string requires 0 substrings and 0 factor
    
    for i in range(n):
        if dp[i][0] == INF:
            continue
            
        current_substrings, current_factor = dp[i]
        
        # Try all possible substrings starting from position i in X
        for j in range(i + 1, n + 1):
            substring = X[i:j]
            substring_len = j - i
            
            # Check if this substring exists in Y
            if substring in Y:
                new_substrings = current_substrings + 1
                new_factor = current_factor + S
                
                if (new_substrings < dp[j][0] or 
                    (new_substrings == dp[j][0] and new_factor < dp[j][1])):
                    dp[j] = (new_substrings, new_factor)
            
            # Check if this substring exists in reversed Y
            if substring in Y_rev:
                new_substrings = current_substrings + 1
                new_factor = current_factor + R
                
                if (new_substrings < dp[j][0] or 
                    (new_substrings == dp[j][0] and new_factor < dp[j][1])):
                    dp[j] = (new_substrings, new_factor)
    
    if dp[n][0] == INF:
        print("Impossible")
    else:
        print(dp[n][1])

solve()