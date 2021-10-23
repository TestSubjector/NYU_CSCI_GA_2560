import argparse
import logging
import sys
import os
from file import handle_file, set_bnf_form
from cnf.cnf import do_cnf
from dpll.dpll import do_dpll

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", const=str, nargs="?")
    parser.add_argument("-i", "--input", const=str, nargs="?")
    parser.add_argument("-mode",const=str, nargs="?", required=True)
    args = parser.parse_args()

    input_data = handle_file(args)

    verbose = False
    if args.v != None:
        verbose = True
    input_form = False
    atom_list = None
    args.mode = args.mode.upper()

    if args.mode == "CNF" or args.mode == "SOLVER":
        input_form, atom_list = do_cnf(input_data, args, verbose)
    if args.mode == "DPLL" or args.mode == "SOLVER":
        if args.mode == "DPLL":
            input_form, atom_list = set_bnf_form(input_data)
            input_form = list(filter(None, input_form))
        do_dpll(input_form, atom_list, verbose)
    if not input_form:
        print("Mode name given to the flag is incorrect. Terminating program")
            
if __name__ == "__main__":
    main()
