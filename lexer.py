# Nickson Dos Santos
# Comp-340 homework_5
# https://github.com/Electronick79/Comp_340.git
import string

lis = list()


class lexer:

    def __init__(self, type, value, lis=None):
        self.type = type
        self.value = value
        lis.append(self)


class lexer(lexer):

    def tonkenize(srcCode, lis=None):
        for scr in srcCode:
            if scr == '(':
                type = "LPAREN"
                value = "("

            elif scr == ')':
                type = "RPAREN"
                value = ")"

            elif scr == '/':
                type = "DIVISION"
                value = "/"

            elif scr == '*':
                type = "MULTIPLICATION"
                value = "*"

            elif scr == '+':
                type = "PLUS"
                value = "+"

            elif scr == '-':
                type = "MINUS"
                value = "-"

            elif scr.isnumeric():
                type = "NUMBERS"
                value = str(scr)

            lexer(type, value)
        return lis
