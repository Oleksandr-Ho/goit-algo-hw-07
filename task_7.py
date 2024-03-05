"""Завдання
Напишіть алгоритм (функцію), який знаходить:
1. Найбільше значення у двійковому дереві 
2. Найменше значення у двійковому дереві
3. Суму всіх значень у двійковому дереві"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# 7_1. Найбільше значення у двійковому дереві
def find_max_value(node):
    current = node
    while current.right:
        current = current.right
    return current.val

# 7_2.Найменше значення у двійковому дереві
def find_min_value(node):
    current = node
    while current.left:
        current = current.left
    return current.val

# 7_3.Суму всіх значень у двійковому дереві
def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(root)
print("Максимальне значення:", find_max_value(root))
print("Мінімальне значення:", find_min_value(root))
print("Сума всіх значень:", sum_of_values(root))