def coin_change(coins, amount):

    # DP array
    dp = [float('inf')] * (amount + 1)

    # Amount 0 requires 0 coins
    dp[0] = 0

    # Fill DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Print DP table
    print("\nDP TABLE")
    print("-" * 50)

    print("Amount : ", end="")
    for i in range(amount + 1):
        print(f"{i:4}", end="")
    print()

    print("DP     : ", end="")
    for value in dp:
        if value == float('inf'):
            print(f"{'-':>4}", end="")
        else:
            print(f"{value:4}", end="")
    print()

    print("-" * 50)

    # Print calculation for every amount
    print("\nCALCULATIONS:")

    for i in range(1, amount + 1):
        print(f"\nAmount {i}:")
        for coin in coins:
            if coin <= i:
                print(
                    f"  Coin {coin}: "
                    f"dp[{i}-{coin}] + 1 = "
                    f"dp[{i-coin}] + 1 = "
                    f"{dp[i-coin]} + 1 = "
                    f"{dp[i-coin] + 1}"
                )

    # Result
    if dp[amount] == float('inf'):
        print("\nAmount cannot be formed.")
    else:
        print(f"\nMinimum number of coins = {dp[amount]}")


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

# Function call
coin_change(coins, amount)