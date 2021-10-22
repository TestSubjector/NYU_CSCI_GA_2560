import argparse
import logging
import sys
import os
from file import set_bnf_form
from cnf.cnf import bnf_to_cnf
from dpll.dpll import dp

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", const=str, nargs="?")
    parser.add_argument("-i", "--input", const=str, nargs="?")
    parser.add_argument("-mode",const=str, nargs="?", required=True)
    args = parser.parse_args()

    # log.warning("Loading Data")

    try:
        input_file = open(args.input or "input.txt", "r")
    except FileNotFoundError:
        print("File input.txt not found. Terminating program")
        exit(0)
    input_data = input_file.read()
    input_file.close()

    verbose = False
    if args.v != None:
        verbose = True

    args.mode = args.mode.upper()
    if args.mode == ("CNF" or "SOLVER"):
        input_form, atom_list = set_bnf_form(input_data)

        cnf_form = bnf_to_cnf(input_form, atom_list)
        cnf_form = [string.split("|") for string in cnf_form]
        for cnf in cnf_form:
            print(*cnf)
    elif args.mode == "DPLL":
        input_form, atom_list = set_bnf_form(input_data)
        # print(input_form)
        # print(atom_list.members)
        table = dp(atom_list.members, input_form, verbose)
        for atom in table:
            print(atom,"=", table[atom])
    else:
        print("Mode name given to the flag is incorrect. Terminating program")
            
if __name__ == "__main__":
    main()
    exit(0)
