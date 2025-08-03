import sys

def solve():
    X = sys.stdin.readline().strip()
    Y = sys.stdin.readline().strip()
    S, R = map(int, sys.stdin.readline().split())
    
    n = len(X)
    m = len(Y)
    
    # Quick impossible check
    if not X:
        print(0)
        return
    
    # Check if all characters in X exist in Y or Y_rev
    Y_chars = set(Y)
    if not all(c in Y_chars for c in X):
        print("Impossible")
        return
    
    Y_rev = Y[::-1]
    
    # dp[i] = (min_substrings, min_factor) to form X[0:i]
    INF = float('inf')
    dp = [(INF, INF) for _ in range(n + 1)]
    dp[0] = (0, 0)
    
    for i in range(1, n + 1):
        # Try substrings of different lengths ending at position i
        # Limit maximum length to avoid excessive computation
        max_len = min(i, m, 100)  # Reasonable upper bound
        
        for length in range(1, max_len + 1):
            j = i - length
            if j < 0 or dp[j][0] == INF:
                continue
                
            substring = X[j:i]
            prev_substrings, prev_factor = dp[j]
            
            # Use Python's efficient substring search
            found_in_Y = substring in Y
            found_in_Y_rev = substring in Y_rev
            
            if not found_in_Y and not found_in_Y_rev:
                continue
            
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