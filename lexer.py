# Nickson Dos Santos
# Comp-340 homework_5

import string


def tokenize(string):  # method tokenize
    lis = []  # empty list to return


for i in range(0, len(string)):  # for every char in the string
    dic = {}  # empty dictionary
if string[i] == "(":  # if char is ( store corresponding type,value in dictionary
    dic["type"] = "LPAREN"
dic["value"] = string[i]  # here the dic looks like { "type" : "LPAREN", "value":"("}
elif string[i] == ")":
dic["type"] = "RPAREN"
dic["value"] = string[i]
elif string[i].isdigit():  # if the char is a digit
if string[i - 1].isdigit():  # if the previous char is a digit continue to next position
    continue

val = ""
while string[i].isdigit():  # while the string[i] is digit add the string[i] to value
    val = val + string[i]
i += 1
dic["type"] = "NUMBER"
dic["value"] = val

elif string[i] == "+":  # checking the char type and adding the type and value to the dictionary
dic["type"] = "PLUS"
dic["value"] = string[i]
elif string[i] == "-":
dic["type"] = "MINUS"
dic["value"] = string[i]
elif string[i] == "*":
dic["type"] = "MULTIPLICATION"
dic["value"] = string[i]
elif string[i] == "/":
dic["type"] = "DIVISION"
dic["value"] = string[i]

dic = dotdict(dic)  # making the dictionary keys,values to be able to access by the Dot(.) operator
lis.append(dic)  # add the dictionary to the list

return lis  # return the list


class dotdict(dict):  # class to make the dictionary values to be able to accessed by DOT(.) operator
    __getattr__ = dict.get




