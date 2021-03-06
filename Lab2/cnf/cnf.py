from atom import atom
from file import set_bnf_form
import copy
from precedence.pred import inf_to_post

def do_cnf(input_data, args, verbose):
    input_form, atom_list = set_bnf_form(input_data)
    input_form = list(filter(None, input_form))

    if args.mode != "CNF":
        verbose = False 
    cnf_form = bnf_to_cnf(input_form, atom_list, verbose)
    cnf_form = [string.split("|") for string in cnf_form]
    if args.mode == "CNF":
        if verbose:
            print("Seperate into sentences")
        for cnf in cnf_form:
            print(*cnf)
    return cnf_form, atom_list

def bnf_to_cnf(input_form, atom_list, verbose):
    cnf_list = []
    for idx, line in enumerate(input_form):
        input_form[idx] = inf_to_post(line)

    if verbose:
        print("Replace <=> & =>")
    for idx, line in enumerate(input_form):
        input_form[idx] = remove_implies(input_form[idx], atom_list).strip().split()
        if verbose:
            print("".join(input_form[idx]))
    
    if verbose:
        print("Apply DeMorgan's")
    for idx, line in enumerate(input_form):
        input_form[idx] = convert_tree(input_form[idx])
        input_form[idx] = handle_negate(input_form[idx])
        if verbose:
            print_tree(input_form[idx])
            print()
    
    if verbose:
        print("Apply distribution")
    for idx, line in enumerate(input_form):
        input_form[idx] = distribute(input_form[idx])
        if verbose:
            print_simpler_tree(input_form[idx])
            print()
    for idx, line in enumerate(input_form):
        input_form[idx] = [cnf_string(input_form[idx])]
        input_form[idx] = input_form[idx][0].split("&")    
        cnf_list += input_form[idx]
    return cnf_list

def remove_implies(postfix, atom_list):
    postfix.reverse()
    stack = []
    token = ""
    while len(postfix) > 0:
        # print(postfix)
        token = postfix.pop()
        if token in atom_list.members:
            stack.append(token)
        elif token == "!":
            neg_token = stack.pop()
            postfix.append(token + " " + "( " + neg_token + " )")
        elif token == "&" or token == "|":
            token_1 = stack.pop()
            token_2 = stack.pop()
            postfix.append(" ( " + token_2 + " " + token + " " + token_1 + " )")
        elif token == "=>":
            token_1 = stack.pop()
            token_2 = stack.pop()
            postfix.append("( " + " ! " +  " ( " + token_2 + " ) " + " | " + token_1 + " ) ")
        elif token == "<=>":
            token_1 = stack.pop()
            token_2 = stack.pop()
            postfix.append(" ( " + " ( " + " ! " +  " ( " + token_2 +  " ) " +  " | " + token_1 + " ) "
            +" & " + "( ! " +  " ( " + token_1 +  " ) " + " | " + token_2 + " ) " + " ) ")
        else:
            stack.append(token)
    return token

def convert_tree(no_implied_string):
    input = no_implied_string
    stack = []
    while len(input) > 0:
        token = input.pop(0)
        if token == "(":
            continue 
        elif token == ")":
            token2 = stack.pop()
            op = stack.pop()
            if op == "!":
                binary = atom.Binary("", op, token2)
                stack.append(binary)
            else:
                binary = atom.Binary(stack.pop(), op, token2)
                stack.append(binary)
        else:
            stack.append(token)
    return stack.pop()

def print_tree(tree):
    if type(tree) == str:
        print(tree, end="")
        return
    if type(tree) is atom.Binary and tree.op != "!":
        print("(", end="")
        print_tree(tree.left)
    print_tree(tree.op)
    print_tree(tree.right)
    if type(tree) is atom.Binary and tree.op != "!":
        print(")", end="")           

def print_simpler_tree(tree):
    if type(tree) == str:
        print(tree, end="")
        return
    if type(tree) is atom.Binary:
        if tree.op == "&" and type(tree.left) is atom.Binary and tree.left.op != "&":
            print("(", end="")
        if tree.op != "!":
            print_simpler_tree(tree.left)
    print_simpler_tree(tree.op)
    print_simpler_tree(tree.right)
    if type(tree) is atom.Binary and tree.op == "&" and type(tree.right) is atom.Binary and tree.right.op != "&":
        print(")", end="")       

def cnf_string(tree):
    string = ""
    if type(tree) == str:
        string = string + tree
        return string   
    if type(tree) is atom.Binary:
        if tree.op != "!":
            string = string + cnf_string(tree.left)
    string = string + cnf_string(tree.op)
    string = string + cnf_string(tree.right)
    return string

def handle_negate(tree):
    if type(tree) is atom.Binary: 
        if tree.op == "!":
            if type(tree.right) == str:
                return tree
            elif type(tree.right) is atom.Binary:
                if tree.right.op == "|":
                    tree.right.op = "&"
                    tree.right.left = handle_negate(atom.Binary("", "!", tree.right.left))
                    tree.right.right = handle_negate(atom.Binary("", "!", tree.right.right))
                    tree = tree.right
                elif tree.right.op == "&":
                    tree.right.op = "|"
                    tree.right.left = handle_negate(atom.Binary("", "!", tree.right.left))
                    tree.right.right = handle_negate(atom.Binary("", "!", tree.right.right))
                    tree = tree.right
                elif tree.right.op == "!":
                    tree = handle_negate(tree.right.right)
                else:
                    print("ERROR: Invalid operator ", tree.right.op, " found. Please resolve.")
                    exit(0)    
        else:
            tree.left = handle_negate(tree.left)
            tree.right = handle_negate(tree.right)
        return tree
    return tree

def distribute(tree):
    if type(tree) is atom.Binary:
        tree.left = distribute(tree.left)
        tree.right = distribute(tree.right)
        if tree.op == "|":
            if type(tree.left) is atom.Binary and tree.left.op == "&":
                left_child = atom.Binary(tree.left.left, "|", tree.right)
                right_child = atom.Binary(tree.left.right, "|", tree.right)
                tree.op = "&"
                tree.left = distribute(left_child)
                tree.right = distribute(right_child)
            elif type(tree.right) is atom.Binary and tree.right.op == "&":
                left_child = atom.Binary(tree.left, "|", tree.right.left)
                right_child = atom.Binary(tree.left, "|", tree.right.right)
                tree.op = "&"
                tree.left = distribute(left_child)
                tree.right = distribute(right_child)
        return tree
    else:
        return tree