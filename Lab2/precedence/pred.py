
def precedence(char:str) -> int:
    return {"<=>": 1, "=>": 2, "|": 3, "&": 4, "!": 5}.get(char, -1)

def inf_to_post(line:str) -> str:
    # Check for equal number of paranthesis
    stack = []
    postfix = []
    for token in line:     
        # print(token)       
        if token == "(":
            stack.append(token)
        elif token == ")":
            while not len(stack) == 0 and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        elif token.isalpha() or token.isdigit():
            postfix.append(token)
        else:
            while not len(stack) == 0 and precedence(token) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(token)
    while not len(stack) == 0:
        postfix.append(stack.pop())
        # print(postfix)
    # return " ".join(postfix)
    return postfix
