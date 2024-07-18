import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def evaluate(self, x):
        return self._evaluate_node(self.root, x)

    def _evaluate_node(self, node, x):
        if node is None:
            return 0

        if node.value == 'x':
            return x
        elif node.value.replace('.', '').isdigit():
            return float(node.value)
        elif node.value in ['+', '-', '*', '/']:
            left = self._evaluate_node(node.left, x)
            right = self._evaluate_node(node.right, x)
            if node.value == '+':
                return left + right
            elif node.value == '-':
                return left - right
            elif node.value == '*':
                return left * right
            elif node.value == '/':
                return left / right
        elif node.value in ['sin', 'cos', 'tan', 'tanh']:
            arg = self._evaluate_node(node.left, x)
            if node.value == 'sin':
                return math.sin(arg)
            elif node.value == 'cos':
                return math.cos(arg)
            elif node.value == 'tan':
                return math.tan(arg)
            elif node.value == 'tanh':
                return math.tanh(arg)

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
                # (sin x) | (x)
                if tokens[0] == '(' and tokens[-1] == ')':
                    return self._create_tree(tokens[1:-1])
                else:
                    return Node(tokens[0])

        node = Node(tokens[operator_index])
        node.left = self._create_tree(tokens[:operator_index])
        node.right = self._create_tree(tokens[operator_index + 1:])
        return node


if __name__ == "__main__":
    expressions = [
        "x + 2",
        "sin x",
        "x * 3 + 2",
        "2 + cos x + 1",
        "2 * x + 3 * x",
        "sin ( ( x + 1 ) + 1 )"
    ]

    x = 1

    for expr in expressions:
        tree = ExpressionTree()
        tree.create_expression_tree(expr)
        result = tree.evaluate(x)
        print(f"Result for '{expr}' with x = {x}: {result}")