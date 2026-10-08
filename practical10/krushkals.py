# Kruskal's Algorithm

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


# Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (source destination weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges by weight
edges.sort()

parent = list(range(n))
rank = [0] * n

mst = []
total_cost = 0

# Kruskal's Algorithm
for weight, u, v in edges:
    x = find(parent, u)
    y = find(parent, v)

    # Add edge only if it does not form a cycle
    if x != y:
        mst.append((u, v, weight))
        total_cost += weight
        union(parent, rank, x, y)

# Output
print("\nEdges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")

print("Total cost of MST:", total_cost)