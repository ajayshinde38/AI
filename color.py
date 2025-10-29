# Create a graph using user input
def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))

    # Take node names
    for i in range(n):
        node = input(f"Enter name of node {i+1}: ")
        graph[node] = []

    # Take edges between nodes
    print("Enter edges (e.g., A B means an edge between A and B). Type 'done' to finish:")
    while True:
        edge = input("Edge: ").split()
        if edge[0].lower() == "done":
            break
        if len(edge) == 2 and edge[0] in graph and edge[1] in graph:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        else:
            print("❌ Invalid edge. Try again.")
    return graph


# Check if it's safe to assign a color
def is_safe(graph, node, color, color_map):
    for neighbor in graph[node]:
        if color_map.get(neighbor) == color:
            return False
    return True


# Recursive function for coloring
def color_graph(graph, colors, color_map, nodes):
    if not nodes:
        return True  # All nodes colored successfully

    node = nodes[0]
    for color in colors:
        if is_safe(graph, node, color, color_map):
            color_map[node] = color
            if color_graph(graph, colors, color_map, nodes[1:]):
                return True
            color_map.pop(node)  # Backtrack
    return False


# Main function
def solve_map_coloring(graph, colors):
    nodes = list(graph.keys())
    color_map = {}

    if color_graph(graph, colors, color_map, nodes):
        return color_map
    return None


# ---- Main Program ----
graph = create_graph()
colors = ["Red", "Green", "Blue", "Yellow"]

solution = solve_map_coloring(graph, colors)

if solution:
    print("\n✅ Map Coloring Solution:")
    for node, color in solution.items():
        print(f"{node}: {color}")
else:
    print("\n❌ No solution exists with the given colors.")
