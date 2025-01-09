"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(10 ** 5, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node

binary_tree: dict[int, BinaryTreeNode] = {}

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:

    full_log_list = []
    node_num = 0

    with open(path_to_log_file, 'r', encoding='utf-8') as file:

        full_log_list = [line.strip() for line in file.readlines()]

    root_node_num = int(full_log_list[0][30:36])
    binary_tree[root_node_num] = BinaryTreeNode(val=root_node_num)
    node_num=root_node_num
    for line in full_log_list[1:]:

        if line.startswith('INFO'):
            node_num = int(line[30:36])
            if binary_tree.get(node_num) is None:
                binary_tree[node_num] = BinaryTreeNode(val=node_num)

        elif line.startswith('DEBUG') and 'left' in line:
            node_left_num = int(line[73:79])
            binary_tree[node_left_num] = BinaryTreeNode(val=node_left_num)
            binary_tree[node_num].left = binary_tree[node_left_num]

        elif line.startswith('DEBUG') and 'right' in line:
            node_right_num = int(line[74:80])
            binary_tree[node_right_num] = BinaryTreeNode(val=node_right_num)
            binary_tree[node_num].right = binary_tree[node_right_num]

    
    return binary_tree[root_node_num]

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )
    # Раскомментировать для перегенерации
    # root = get_tree(7)
    # walk(root)

    root_restored = restore_tree('walk_log_4.txt')
    print(restore_tree('walk_log_4.txt'))
