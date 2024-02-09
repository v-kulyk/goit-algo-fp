import heapq
import random
from collections import deque
from math import floor

from task_4 import Node, draw_tree, build_heap_tree


def traverse_tree_bfs(root, colors:list):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        current_node.color = colors.pop(0)
        result.append(current_node)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


def traverse_tree_dfs(root:Node, colors:list):
    def dfs_helper(node, result):
        if node:
            node.color = colors.pop(0)
            result.append(node)
            dfs_helper(node.left, result)
            dfs_helper(node.right, result)

    result = []
    dfs_helper(root, result)
    return result


def generate_gradient_shades_of_red_rgb(num_colors=10):
    colors = [(255, floor(240 * i / num_colors), floor(240 * i / num_colors)) for i in range(num_colors)]

    hex_colors = [f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}' for color in colors]

    return hex_colors



if __name__ == '__main__':
    heap = [random.randint(1, 100) for _ in range(16)]
    heapq.heapify(heap)
    root = build_heap_tree(heap)

    # BFS
    colors = generate_gradient_shades_of_red_rgb(len(heap))
    bfs_result = traverse_tree_bfs(root, colors)
    draw_tree(root)

    # DFS
    colors = generate_gradient_shades_of_red_rgb(len(heap))
    dfs_result = traverse_tree_dfs(root, colors)
    draw_tree(root)
