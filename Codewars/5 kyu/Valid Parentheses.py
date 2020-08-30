def valid_parentheses(string):
    par=''
    for char in string:
        if char =='(' or char ==')':
            par+=char
    mod=True
    while mod:
        if not par:
            return True
        mod=False
        for i in range(len(par)//2):
            print(par)
            if par[i]=='(' and par[i+1]==')':
                par=par[:i]+par[i+2:]
                mod=True
                break

        continue
        if par[0]=='(' and par[-1]==')':
            par=par[1:-1]
    if par:
        return False


print(valid_parentheses("()()()"))














'''Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).'''
