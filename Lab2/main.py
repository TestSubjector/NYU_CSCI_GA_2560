import argparse
import logging
import sys
import os
from file import set_form
from precedence.pred import inf_to_post
from cnf.cnf import distribute, handle_negate, print_tree, print_simpler_tree, remove_implies, convert_tree

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", const=str, nargs="?")
    parser.add_argument("-i", "--input", const=str, nargs="?")
    args = parser.parse_args()

    log.warning("Loading Data")

    try:
        input_file = open(args.input or "input.txt", "r")
    except FileNotFoundError:
        print("File input.txt not found. Terminating program")
        exit(0)
    input_data = input_file.read()
    input_file.close()

    input_form, atom_list = set_form(input_data)

    verbose = False
    if args.v != None:
        verbose = True

    for idx, line in enumerate(input_form):
        postfix_line = inf_to_post(line)
        print(postfix_line)
        input_form[idx] = remove_implies(postfix_line, atom_list).strip().split()
        print(" ".join(input_form[idx]))
        input_form[idx] = convert_tree(input_form[idx], atom_list)
        input_form[idx] = handle_negate(input_form[idx])
        print_tree(input_form[idx])
        print()
        input_form[idx] = distribute(input_form[idx])
        print_simpler_tree(input_form[idx])
        print()
            
if __name__ == "__main__":
    main()
