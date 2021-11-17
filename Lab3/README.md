# CSCI-GA.2560 Lab 3

Contains the code for
* Markov Process Solver

## Dependencies

* python3

## Run Code

### Format

```
python3 path/to/main.py [-min] -df $df -tol $tolerance -i $input-file
```

### Examples

```
python3 main.py -tol 0.001 -df 0.9 -i input6.txt
```

```
python3 main.py -min -tol 0.001 -i input3.txt
``` 

## Command line flags
 
Below are the list of command-line flags required and accepted by this project.

```
--input (-i) <path>: The input file containing the graph to be searched.  
-min : If given, minimises values as costs. Does not have any argument.   
-df : Discount factor. Argument should be between 0 & 1
-tol : Float tolerance 
```

## Author

Kumar Prasun (kp2692)