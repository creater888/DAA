"""
Problem: 0/1 Knapsack Problem using Dynamic Programming
Algorithm: Bottom-Up DP Table Construction & Item Backtracking
Time Complexity: O(n * W)
Space Complexity: O(n * W)
"""

def solve_knapsack(n: int, W: int, weights: list[int], values: list[int]):
    # dp[i][w] stores maximum value for 'i' items with capacity 'w'
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build the DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Display the DP Matrix
    print("\n" + "=" * 44)
    print("             DP TABLE COMPUTED              ")
    print("=" * 44)
    
    header = "Item\\Cap |" + "".join(f"{w:>5}" for w in range(W + 1))
    print(header)
    print("---------+" + "-" * ((W + 1) * 5))

    for i in range(n + 1):
        row_str = f"{i:>7}  |" + "".join(f"{dp[i][w]:>5}" for w in range(W + 1))
        print(row_str)

    # Backtracking to find the exact items included
    selected_items = []
    res = dp[n][W]
    current_weight = W
    total_weight_used = 0

    for i in range(n, 0, -1):
        if res <= 0:
            break
        # If value came from the included item state
        if res != dp[i - 1][current_weight]:
            selected_items.append(i)  # 1-based item index
            total_weight_used += weights[i - 1]
            res -= values[i - 1]
            current_weight -= weights[i - 1]

    # Display Final Results
    print("\n" + "=" * 44)
    print("                  RESULT                    ")
    print("=" * 44)
    print(f"Maximum Achievable Value: {dp[n][W]}")
    print(f"Total Weight Utilized   : {total_weight_used} / {W}")
    print("Selected Items (1-based): ", end="")

    if not selected_items:
        print("None")
    else:
        selected_items.reverse()
        formatted_items = [
            f"Item {idx} (wt: {weights[idx - 1]}, val: {values[idx - 1]})"
            for idx in selected_items
        ]
        print("  ".join(formatted_items))
        
    print("=" * 44)


def main():
    print("================ 0/1 KNAPSACK DP ================")
    
    try:
        n = int(input("Enter the number of items: "))
        if n <= 0:
            print("Invalid item count.")
            return
    except ValueError:
        print("Invalid item count.")
        return

    try:
        W = int(input("Enter knapsack capacity: "))
        if W <= 0:
            print("Invalid knapsack capacity.")
            return
    except ValueError:
        print("Invalid knapsack capacity.")
        return

    weights = []
    values = []

    print("\nEnter weight and value for each item:")
    for i in range(n):
        try:
            wt, val = map(int, input(f"Item {i + 1} [Weight Value]: ").split())
            weights.append(wt)
            values.append(val)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            return

    solve_knapsack(n, W, weights, values)


if __name__ == "__main__":
    main()