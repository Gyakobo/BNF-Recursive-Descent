# BNF with Recursive Descent

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

>[!NOTE]
>Please feel free to make pull requests and edit this project to your will.

## Introduction

[Backus-Naur Form (BNF)](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) is a notation technique used to describe the grammar of a language in a formal and concise way. It defines the syntax of programming languages, data structures, and protocols. A BNF grammar consists of a set of production rules that define how strings in the language can be generated. Each rule describes how a symbol can be replaced with a sequence of other symbols.

For example, the BNF for arithmetic expressions might look like this:

```php
<expression> ::= <term> + <expression> | <term> - <expression> | <term>
<term> ::= <factor> * <term> | <factor> / <term> | <factor>
<factor> ::= (<expression>) | <operand>
<operand> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

In this BNF, an `<expression>` can be a `<term>` followed by + and another `<expression>`, or a `<term>` followed by - and another `<expression>`, or just a `<term>`. A `<term>` can be a `<factor>` followed by * and another `<term>`, and so on. This recursive definition allows complex expressions to be built from simpler components.

[Recursive Descent Parsing](https://en.wikipedia.org/wiki/Recursive_descent_parser) is a top-down parsing technique that uses a set of recursive functions to process the input string and build a parse tree according to the grammar defined by the BNF. Each non-terminal symbol in the BNF corresponds to a function in the parser. These functions call each other recursively to parse the input and build the syntax tree.

For example, given the BNF rules above, a recursive descent parser would have functions like `parse_expression`, `parse_term`, `parse_factor`, and `parse_operand`. Each function is responsible for parsing its corresponding non-terminal symbol.

### Example

Here is a simple example of how recursive descent parsing works:

1. *parse_expression*: This function would try to parse a `<term>`, then check if there is a `+` or `-` operator, and if so, recursively parse another `<expression>`.

1. *parse_term*: This function would try to parse a `<factor>`, then check if there is a `*` or `/` operator, and if so, recursively parse another `<term>`.

1. *parse_factor*: This function would check if the input starts a `(`, and if so, recursively parse an `<expression>` inside the parentheses. If not, it would try to parse an `<operand>`.

1. *parse_operand*: This function would simply check if the current character is a digit and return it as an operand.

By following these steps, a recursive descent parser can build a tree structure that represents the syntactic structure of the input string. This tree can then be used to evaluate the expression, generate ocde, or perform other tasks.

Recursive descent parsing is straightforward to implement and understand, making it a good choice for simple grammars. However, it may not be efficient for more complex grammars due to its potential for exponential time complexity in certain cases.

## Methodology

This project aims to parse and evaluate arithmetic expressions using recursive descent parsing based on BNF (Backus-Naur Form) grammar rules. The process involves defining a grammar, implementing a parser, constructing an expression tree, and evaluating the tree.

1. *Defining the Grammar*:

The BNF grammar for arithmetic expressions is defined as follows:

```html
<expression> ::= <term> + <expression> | <term> - <expression> | <term>
<term> ::= <factor> * <term> | <factor> / <term> | <factor>
<factor> ::= (<expression>) | <operand>
<operand> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

This grammar describes how complex arithmetic expressions can be built from simpler components.

2. *Implementing the Parser*:

The parser is implemented using recursive descent parsing. Each non-terminal symbol in the grammar corresponds to a function in the parser. 

* Parser Class: Ther `Parser` class handles the parsing of the input string.

```python
class Parser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")
        self.position = 0
```

* Parsing Expressions: The `parse_expression` function parses an `<expression>`.

```python
def parse_expression(self):
    left = self.parse_term()
    while self.current_char() in ('+', '-'):
        operator = self.current_char()
        self.advance()
        right = self.parse_term()
        left = ExpressionNode(left, operator, right)
    return left
```

* Parsing Terms: The `parse_term` function parses a `<term>`.

```python
def parse_term(self):
    left = self.parse_factor()
    while self.current_char() in ('*', '/'):
        operator = self.current_char()
        self.advance()
        right = self.parse_factor()
        left = TermNode(left, operator, right)
    return left
```

* Parsing Factors: The `parse_factor` function parses a `<factor>`

```python
def parse_factor(self):
    if self.current_char() == '(':
        self.advance()
        expr = self.parse_expression()
        if self.current_char() == ')':
            self.advance()
        return FactorNode(expr)
    else:
        return self.parse_operand()
```

* Parsing Operands: The `parse_operand` function parses an `<operand>`.

```python
def parse_operand(self):
    start = self.position
    while self.current_char() is not None and self.current_char().isdigit():
        self.advance()
    value = int(self.input[start:self.position])
    return OperandNode(value)
```

## License
MIT

