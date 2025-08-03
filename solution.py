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
    dp = [(INF, INF) for _ in range(n + 1)]
    dp[0] = (0, 0)  # Empty string needs 0 substrings and 0 factor
    
    for i in range(1, n + 1):
        # Try all possible last substrings ending at position i
        for j in range(i):
            if dp[j][0] == INF:
                continue
                
            substring = X[j:i]
            substring_len = len(substring)
            
            # Check if substring exists in Y
            found_in_Y = False
            found_in_Y_rev = False
            
            # Check in normal Y
            for k in range(m - substring_len + 1):
                if Y[k:k + substring_len] == substring:
                    found_in_Y = True
                    break
            
            # Check in reversed Y
            for k in range(m - substring_len + 1):
                if Y_rev[k:k + substring_len] == substring:
                    found_in_Y_rev = True
                    break
            
            # Update dp[i] if we can form X[0:i]
            if found_in_Y or found_in_Y_rev:
                prev_substrings, prev_factor = dp[j]
                
                # Try using substring from normal Y
                if found_in_Y:
                    new_substrings = prev_substrings + 1
                    new_factor = prev_factor + S
                    
                    if (new_substrings < dp[i][0] or 
                        (new_substrings == dp[i][0] and new_factor < dp[i][1])):
                        dp[i] = (new_substrings, new_factor)
                
                # Try using substring from reversed Y
                if found_in_Y_rev:
                    new_substrings = prev_substrings + 1
                    new_factor = prev_factor + R
                    
                    if (new_substrings < dp[i][0] or 
                        (new_substrings == dp[i][0] and new_factor < dp[i][1])):
                        dp[i] = (new_substrings, new_factor)
    
    if dp[n][0] == INF:
        print("Impossible")
    else:
        print(dp[n][1])

solve()