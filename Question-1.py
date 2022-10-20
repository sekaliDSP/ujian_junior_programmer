#hello for this script i write it and run it on python 3.10 version

def BracketCheck(InputtedString):
    OpenBracket = ["[","(","{"]
    CloseBracket = ["]",")","}"]
    Stack = []
    for i in InputtedString:
        if i in OpenBracket:
            Stack.append(i)
        elif i in CloseBracket:
            position = CloseBracket.index(i)
            if ((len(Stack)>0) and
                (OpenBracket[position] == Stack[len(Stack)-1])):
                Stack.pop()
            else:
                return "False"
    if len(Stack) == 0:
        return "True"
    else:
        return "False"

InputString = input("Input The Word to check are the brackets have balanced open/close tag or not.. ")

print(BracketCheck(InputString))
