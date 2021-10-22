from atom import atom

def set_bnf_form(graph_data):
    atom_list = atom.Atom()
    splitdata = graph_data.split("\n")
    for idx, line in enumerate(splitdata):
        splitdata[idx] = line.strip().split()
        for token in splitdata[idx]:
            if token not in ["<=>", "=>", "&", "!", "|"]:
                if "!" in token:
                    atom_list.members.add(token.replace("!", ""))
                else:    
                    atom_list.members.add(token)
    atom_list.members = list(atom_list.members)
    atom_list.members.sort()
    return splitdata, atom_list
