def construct_subsequence(path, A, i, j, k, l):
    if i is None or j is None or k is None or l is None or path[i][j][k][l] is None:
        return ""
    
    ni, nj, nk, nl = path[i][j][k][l]
    if (ni, nj, nk, nl) == (i+1, j-1, k+1, l-1):  # Match
        return A[i] + construct_subsequence(path, A, ni, nj, nk, nl) + A[j]
    else:  # Follow the best path
        return construct_subsequence(path, A, ni, nj, nk, nl)


def bottom_up_lcps(A, B):
    n = len(A)
    # Initialize a 4D DP array
    lcps_arr = [[[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    path = [[[[None for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

    # Base case: single character palindromes
    for i in range(n):
        for k in range(n):
            if A[i] == B[k]:
                lcps_arr[i][i][k][k] = 1
                path[i][i][k][k] = (None, None, None, None)  # No further backtracking

    # Fill the table for larger subsequences
    for a_len in range(1, n+1):
        for b_len in range(1, n+1):
            for i in range(n - a_len + 1):
                for k in range(n - b_len + 1):
                    j = i + a_len - 1
                    l = k + b_len - 1
                    if A[i] == A[j] == B[k] == B[l]:
                        lcps_arr[i][j][k][l] = 2 + lcps_arr[i+1][j-1][k+1][l-1]
                        path[i][j][k][l] = (i+1, j-1, k+1, l-1)
                    else:
                        options = [
                            (lcps_arr[i+1][j][k][l], (i+1, j, k, l)),
                            (lcps_arr[i][j-1][k][l], (i, j-1, k, l)),
                            (lcps_arr[i][j][k+1][l], (i, j, k+1, l)),
                            (lcps_arr[i][j][k][l-1], (i, j, k, l-1)),
                        ]
                        lcps_arr[i][j][k][l], path[i][j][k][l] = max(options)

    # Reconstruct the subsequence
    lcps_subsequence = construct_subsequence(path, A, 0, n-1, 0, n-1)
    return lcps_arr[0][n-1][0][n-1], lcps_subsequence


# Example usage:
A = "ashfghsa"
B = "sahiyhas"
lcps_length, lcps_subsequence = bottom_up_lcps(A, B)
print("Bottom-Up LCPS Length:", lcps_length)
print("Bottom-Up LCPS Subsequence:", lcps_subsequence)
