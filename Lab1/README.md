# CSCI-GA.2560 Lab 1

Contains the code for three search algorithms
* Breadth First Search
* Iterative Deepening Search
* A* Search

## Dependencies

* python3

## Run Code

### Format

```
python3 path/to/main.py [-v] -start $start-node -goal $goal-node -alg $alg [-depth $depth] graph-file
```

### Examples

#### For Breadth First Search

```
python3 main.py -start S -goal G -alg bfs -i input3.txt -v
```

#### For Iterative Deepening Search (Start depth = 2)

```
python3 main.py -start S -goal G -alg ids -depth 2 --input input_file.txt -v
``` 

#### For A*

```
python3 main.py -start S -goal G -alg astar -i random_name.txt -v
```


## Command line flags
 
Below are the list of command-line flags required and accepted by this project.

```
--input (-i) <path>: The input file containing the graph to be searched.  
-start : The starting node of the graph.  
-goal (-end):  Name of the node which is the goal.  
-alg : Name of the algorithm, not case sensitive. Can be   one of the following: *ids, bfs, astar*.  
-depth: Required when -alg is set to *astar*, otherwise is ignored.  
-v : Verbose output
```

## Author

Kumar Prasun (kp2692)
