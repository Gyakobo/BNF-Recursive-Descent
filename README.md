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


