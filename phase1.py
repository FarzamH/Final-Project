import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def create_expression_tree(self, expression):
        tokens = expression.split()
        self.root = self._create_tree(tokens)

    def _create_tree(self, tokens):
        if not tokens:
            return None

        if len(tokens) == 1:
            return Node(tokens[0])

        operator_index = -1
        parentheses_count = 0
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] == ')':
                parentheses_count += 1
            elif tokens[i] == '(':
                parentheses_count -= 1
            elif parentheses_count == 0:
                if tokens[i] in ['+', '-']:
                    operator_index = i
                    break
                elif tokens[i] in ['*', '/'] and operator_index == -1:
                    operator_index = i

        if operator_index == -1:
            if tokens[0] in ['sin', 'cos', 'tan', 'tanh']:
                node = Node(tokens[0])
                node.left = self._create_tree(tokens[1:])
                return node
            else:
                if tokens[0] == '(' and tokens[-1] == ')':
                    return self._create_tree(tokens[1:-1])
                else:
                    return Node(tokens[0])

        node = Node(tokens[operator_index])
        node.left = self._create_tree(tokens[:operator_index])
        node.right = self._create_tree(tokens[operator_index + 1:])
        return node

expressions = [
    "x + y",
    "sin x * cos y",
    "z * 3 + x * y",
    "tanh ( x + y ) * z"
]

for expr in expressions:
    tree = ExpressionTree()
    tree.create_expression_tree(expr)
    print(f'tree {tree} with expression {expr} created successfully.')