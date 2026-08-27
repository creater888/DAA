def matrix_chain_order(p):

    n = len(p) - 1

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Store split positions
    split = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    # Print DP table
    print("\nMATRIX CHAIN MULTIPLICATION TABLE")
    print()

    print("      ", end="")

    for j in range(1, n + 1):
        print(f"{j:8}", end="")

    print()

    print("    " + "-" * (8 * n))

    for i in range(1, n + 1):

        print(f"{i} | ", end="")

        for j in range(1, n + 1):

            if i > j:
                print(f"{' ':8}", end="")
            else:
                print(f"{dp[i][j]:8}", end="")

        print()

    print("\nMinimum number of scalar multiplications =", dp[1][n])


# Matrix dimensions
p = [10, 20, 30, 40, 30]

matrix_chain_order(p)