# Prim's Algorithm

INF = 999999

# Number of vertices
n = int(input("Enter number of vertices: "))

# Adjacency matrix
graph = []

print("Enter the adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

# Track selected vertices
selected = [False] * n
selected[0] = True

total_cost = 0

print("\nEdges in Minimum Spanning Tree:")

for _ in range(n - 1):
    minimum = INF
    x = 0
    y = 0

    # Find the minimum edge connecting
    # selected and unselected vertices
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {minimum}")

    total_cost += minimum
    selected[y] = True

print("Total cost of MST:", total_cost)