from atom import atom

def set_bnf_form(graph_data):
    atom_list = atom.Atom()
    splitdata = graph_data.split("\n")
    for idx, line in enumerate(splitdata):
        for op in ["<=>", "&", "|", "(", ")"]:
            line = line.replace(op, " " + op + " ")   
        splitdata[idx] = line.strip().split()
        for token in splitdata[idx]:
            if token not in ["<=>", "=>", "&", "!", "|", "(", ")"]:
                if "!" in token:
                    atom_list.members.add(token.replace("!", ""))
                else:    
                    atom_list.members.add(token)
    atom_list.members = list(atom_list.members)
    atom_list.members.sort()
    return splitdata, atom_list

def handle_file(args):
    try:
        input_file = open(args.input or "input.txt", "r")
    except FileNotFoundError:
        print("File input.txt not found. Terminating program")
        exit(0)

    input_data = input_file.read()
    input_file.close()
    return input_data