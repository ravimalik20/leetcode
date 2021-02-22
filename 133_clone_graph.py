class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_nodes_index = dict()
        stk = list()
        stk.extend(node.neighbors)

        visited = set()

        while len(stk) > 0:
            top = stk.pop()

            if top.val in visited:
                continue
            else:
                visited.add(top.val)

            if top.val not in new_nodes_index:
                n = Node(top.val)
                new_nodes_index[top.val] = n
            else:
                n = new_nodes_index[top.val]

            for neighbor in top.neighbors:
                if neighbor.val not in new_nodes_index:
                    new_nodes_index[neighbor.val] = Node(neighbor.val)

                n.neighbors.append(new_nodes_index[neighbor.val])

        return new_nodes_index[node.val]
