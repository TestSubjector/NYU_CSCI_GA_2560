from atom import atom

def set_form(graph_data):
    atom_list = atom.Atom()
    splitdata = graph_data.split("\n")
    for idx, line in enumerate(splitdata):
        splitdata[idx] = line.strip().split()
        for token in splitdata[idx]:
            if token not in ["<=>", "=>", "&", "!", "|"]:
                atom_list.members.add(token)
    return splitdata, atom_list
