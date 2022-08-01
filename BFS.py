def BFS(node, graph):
	visited = []
	queue = []
	visited += [node]
	queue.append(node)
	while queue:
#		for i in len(queue):
		current = queue.pop(0)
		for neighbors in graph[current]:
			if neighbor not in visited:
				queue.append(neighbor)
				visited.append(neighbor)


def bfs(self, root=None):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        cur_node = queue.pop(0)

        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)

    # end

