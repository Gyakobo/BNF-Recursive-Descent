'''
The overall BNF and Parse Tree Description:

<expression>  ::=  <term>  + <expression>   |   <term>  -  <expression>   |   <term>
<term>  :=  <factor> * <term> | <factor> / <term> | <factor>
<factor>  ::=  (  <expression>  )  |  <operand>
<operand>  ::=  0|1|2|3|4|5|6|7|8|9
'''

class OperandNode():
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class FactorNode():
    def __init__(self, child):
        self.child = child

    def evaluate(self):
        return self.child.evaluate()

class TermNode():
    def __init__(self, left, operator = None, right = None):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        if not self.operator:
            return self.left.evaluate()
        elif self.operator == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.operator == '/':
            return self.left.evaluate() / self.right.evaluate()

class ExpressionNode():
    def __init__(self, left, operator = None, right = None):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        if not self.operator:
            return self.left.evaluate()
        elif self.operator == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.operator == '-':
            return self.left.evaluate() - self.right.evaluate()

class Parser:
    def __init__(self, input_string):
        # Getting rid of the spaces entirely
        self.input = input_string.replace(' ', '')

        # Set position 
        self.position = 0
    
    def parse_expression(self):
        left = self.parse_term()
        while self.current_char() == '+' or self.current_char() == '-':
            operator = self.current_char()
            self.advance()
            right = self.parse_term()
            left = ExpressionNode(left, operator, right)
        return left

    def parse_term(self):
        left = self.parse_fator()
        while self.current_char() == '*' or self.current_char() == '/':
            operator = self.current_char()
            self.advance()
            right = self.parse_fator()
            left = TermNode(left, operator, right)
        return left

    def parse_fator(self):
        if self.current_char() == '(':
            self.advance()
            expr = self.parse_expression()
            if self.current_char() == ')':
                self.advance()

            return FactorNode(expr)

        else:
            return self.parse_operand()

    def parse_operand(self):
        start = self.position
        while self.current_char() is not None and self.current_char().isdigit():
            self.advance()
        value = int(self.input[start:self.position])
        return OperandNode(value)

    def current_char(self):
        if self.position >= len(self.input):
            return None
        return self.input[self.position]

    def advance(self):
        self.position += 1

# Builds the expression tree
def expression_evaluation(input_string):
    parser = Parser(input_string)
    tree = parser.parse_expression()
    return tree.evaluate()

# Usage

input_string = input("Please enter expression: ")

if not input_string: 
    input_string = "5 + 3 * 8" # Ans: 29

result = expression_evaluation(input_string)
print(f'Input Expression: {input_string}')
print(f'Result: {result}')
