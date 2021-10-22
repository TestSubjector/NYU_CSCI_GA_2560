import copy

def dp(atoms, sentences, verbose):
    table = dict()
    for A in atoms:
        table[A] = None;
    return dp1(atoms,sentences,table, verbose)

def dp1(atoms,sentences,table, verbose):
    loop = True
    while loop:
        # print("Entering loop")
        loop = False
        # Failed Case
        for clause in sentences:
            if len(clause) == 0:
                return None
        # Empty Sentence
        if len(sentences) == 0:   
            for A in atoms:
                if table[A] == None:
                    if verbose: 
                        print("Unbound ", A, "= False")
                    table[A] = False
            return table
        for clause in sentences:
            if len(clause) == 1:
                print_cnf(sentences, verbose)
                table = obvious_assign(clause[0], table, verbose)
                sentences = propagate(clause[0], sentences, table)
                loop = True
                break
        # Pure Literal
        for atom in atoms:
            has_atom = False
            has_neg_atom = False
            neg_atom = "!" + atom
            for clause in sentences:
                # print(atom, " ",has_atom, " ", has_neg_atom, " ", clause)
                if atom in clause:
                    has_atom = True
                if neg_atom in clause:
                    has_neg_atom = True
            if has_atom and not has_neg_atom:
                print_cnf(sentences, verbose)
                if verbose:
                    print("Easy case ", atom, "= True")
                table[atom] = True
                sentences = set_and_remove(atom, sentences, loop)
            elif not has_atom and has_neg_atom:
                print_cnf(sentences, verbose)
                if verbose:
                    print("Easy case ", atom, "= False")
                table[atom] = False
                sentences = set_and_remove(neg_atom, sentences, loop)
    
    new_sentences = copy.deepcopy(sentences)
    new_table = copy.deepcopy(table)
    picked = None
    for atom in atoms:
        if table[atom] == None:
            new_table[atom] = True
            picked = atom
            break
    print_cnf(sentences, verbose)
    if verbose:
        print("Hard guess ", atom, "= True")
    new_sentences = propagate(picked, new_sentences, new_table)
    new_table = dp1(atoms, new_sentences, new_table, verbose)
    if new_table != None:
        return new_table
    else:
        print_cnf(sentences, verbose)
        if verbose:
            print("Fail hard guess, try: ", atom, "= False")
        new_sentences = copy.deepcopy(sentences)
        new_table = copy.deepcopy(table)
        new_table[picked] = False
        new_sentences = propagate(picked, new_sentences, new_table)
        return dp1(atoms, new_sentences, new_table, verbose)

 
def propagate(atom, sentences, table):
    if is_neg(atom):
        neg_atom = atom.replace("!","")
    else:
        neg_atom = "!" + atom
    for idx, clause in enumerate(sentences):
        if (atom in clause and table[atom] == True) or (neg_atom in clause and table[atom] == False):
            sentences[idx] = []
        elif atom in clause and table[atom] == False:
            sentences[idx].remove(atom)
        elif neg_atom in clause and table[atom] == True:
            sentences[idx].remove(neg_atom)
    new_sentences = list(filter(None, sentences))
    return new_sentences

def set_and_remove(atom, sentences, loop):
    loop = True
    for clause in sentences:
        if atom in clause:
            sentences.remove(clause)
    return sentences

def is_neg(atom):
    if "!" in atom:
        return True
    return False

def obvious_assign(atom, table, verbose):
    if is_neg(atom):
        if verbose:
            print("Easy case ", atom.replace("!",""), "= False")
        table[atom.replace("!","")] = False
    else:
        if verbose:
            print("Easy case ", atom, "= True")
        table[atom] = True
    return table

def print_cnf(sentences, verbose):
    if verbose:
        for clause in sentences:
            print(*clause)