def knapsack():
    n = int(input("Enter the number of items: "))
    ls = [tuple(map(int, input(f"Enter weight and price of item {i+1}: ").split())) for i in range(n)]
    w = int(input("Enter the maximum weight capacity: "))

    # Sort items by weight
    ls.sort(key=lambda x: x[0])

    # Initialize DP table
    arr = [[0] * (w + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if ls[i - 1][0] <= j:
                arr[i][j] = max(ls[i - 1][1] + arr[i - 1][j - ls[i - 1][0]], arr[i - 1][j])
            else:
                arr[i][j] = arr[i - 1][j]

    # Find items to include in the knapsack
    res, items = arr[n][w], []
    j = w
    for i in range(n, 0, -1):
        if arr[i][j] != arr[i - 1][j]:
            items.append(ls[i - 1])
            j -= ls[i - 1][0]

    # Print results
    print("Items included in the knapsack are:", items)
    print("Total price:", res)

if __name__ == "__main__":
    knapsack()
