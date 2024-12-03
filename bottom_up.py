import numpy as np
import time


def longest_common_palindromic_subsequence(S1, S2):
    m, n = len(S1), len(S2)

    # Create a 4D DP table initialized to zero
    dp = np.zeros((m + 1, n + 1, m + 1, n + 1), dtype=int)

    # Fill the DP table
    for length1 in range(1, m + 1):
        for length2 in range(1, n + 1):
            for i in range(m - length1 + 1):
                for j in range(n - length2 + 1):
                    # Check if we can form a palindrome
                    if S1[i] == S2[j]:
                        dp[length1][length2][i][j] = dp[length1-1][length2-1][i+1][j+1] + 1
                    else:
                        dp[length1][length2][i][j] = max(dp[length1-1][length2][i+1][j], dp[length1][length2-1][i][j+1])

    # The length of the longest common palindromic subsequence
    return dp[m][n][0][0]

# Example usage
def test_lcps():
    test_cases = [
        ("aahiyhas", "aashjjjs"),  # Your specific test case
        ("ABCD", "ACDF"),          # Basic test
        ("AGGTAB", "GXTXAYB"),     # Another test
        ("HELLO", "WORLD"),        # Different test
        ("AAA", "AAA"),            # Repeated characters
        ("AsAeA", "AgAeA"),                  # Empty strings
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321", "123456789abcdefghijklmnopqrstuvwxyz")
    ]
    
    for x, y in test_cases:
        print(f"LCS Length of {x} and {y}: {longest_common_palindromic_subsequence(x, y)}")


test_lcps()