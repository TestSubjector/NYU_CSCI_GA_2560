# CSCI-GA.2560 Lab 2

Contains the code for three modes

* A generic DPLL solver
* A BNF to CNF converter
* Takes BNF and solves it by running the above two steps

## Dependencies

* python3

## Run Code

### Format

```shell
python3 path/to/main.py [-v] -mode $mode -i graph-file
```

### Examples

#### For DPLL

```shell
python3 main.py -mode dpll -i input.txt -v
```

#### For BNF to CNF converter

```shell
python3 main.py -mode cnf --input input_file.txt -v
``` 

#### For BNF to DPLL

```shell
python3 main.py -mode solver -i random_name.txt -v
```

## Command line flags
 
Below are the list of command-line flags required and accepted by this project.

```shell
--input (-i) <path>: The input file containing the graph to be searched.   
-mode: Name of the mode, not case sensitive. Can be one of the following: *cnf, dpll, solver*.   
-v : Verbose output
```

## Author

Kumar Prasun (kp2692)