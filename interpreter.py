from typing import List
from node import Node
from tokens import AtomType, BuiltIn

class Interpreter:
    def __init__(self):
        self.BUILT_IN = {
            BuiltIn.ADD : self.add,
            BuiltIn.QUOTE : self.quote
        }

    def evaluateExpressions(self, expressions : List[Node]) -> List[Node]:
        results = []
        for expression in expressions:
            results.append(self.evaluateExpression(expression))
        return results

    def evaluateExpression(self, expression: Node) -> Node:
        # expression: BuiltIn, Atom, Symbol
        if expression.type in AtomType:
            if expression.type == AtomType.SYMBOL:
                # Handle symbols
                print("NA")
            elif expression.type == AtomType.LIST:
                print("is list")
            return expression
        return self.BUILT_IN[expression.type](expression)

    def add(self, expression: Node) -> Node:
        sum = 0
        for child in expression.children:
            sum += self.evaluateExpression(child).val
        return Node(sum, AtomType.NUMBER)

    def quote(self, expression: Node) -> Node:
        return expression.children[0]
