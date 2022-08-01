def DFS(Node,root):
	if root:
		return False
	else:
		visited[root] = True
		for node in root.adjacentcy_list:
			if visted[node] == False:
				DFS(node)

## Convert sorted array to BST
