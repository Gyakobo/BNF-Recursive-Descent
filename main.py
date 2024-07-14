'''
The overall BNF:

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

