import time
from sortedcontainers import SortedDict  # For sparse storage (balanced tree equivalent)


def sparse_lcps(S1, S2):
    m, n = len(S1), len(S2)
    # Sparse storage for DP fragments
    dp = SortedDict()

    # Helper function to compute LCS for fragments
    def compute_lcs(i1, j1, i2, j2):
        key = (i1, j1, i2, j2)
        if key in dp:
            return dp[key]
        
        if i1 > i2 or j1 > j2:
            return 0
        
        if S1[i1] == S2[j1]:
            result = 1 + compute_lcs(i1 + 1, j1 + 1, i2, j2)
        else:
            result = max(compute_lcs(i1 + 1, j1, i2, j2), compute_lcs(i1, j1 + 1, i2, j2))
        
        dp[key] = result
        return result

    # Iterate over fragments in a sparse manner
    for i in range(m):
        for j in range(n):
            if S1[i] == S2[j]:  # Only process likely palindromic starting points
                dp[(i, j, m - 1, n - 1)] = compute_lcs(i, j, m - 1, n - 1)
    
    # Maximum length of LCPS
    return max(dp.values(), default=0)


# Example usage
def test_sparse_lcps():
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
        print(f"Sparse LCPS Length of {x} and {y}: {sparse_lcps(x, y)}")


test_sparse_lcps()
