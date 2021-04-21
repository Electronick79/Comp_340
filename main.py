# Nickson Dos Santos
# Comp-340 homework_5
#https://github.com/Electronick79/Comp_340.git

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(lexer):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {lexer}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import lexer

srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.tokenize(srcCode)

for i in tokSeq:
    print(i.type, i.value)

