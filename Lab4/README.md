# CSCI-GA.2560 Lab 4

Contains the code for
* knn
* kmeans

## Dependencies

* python3

## Run Code

### Format

We have a `-mode` argument for selecting knn or kmeans algorithm.

For running knn
```
python3 path/to/main.py -mode knn -train $train_file.txt -test $test_file.txt -k k_value -d e2/manh -unitw True/False
```

For running kmeans
```
python3 path/to/main.py [-min] -df $df -tol $tolerance -i $input-file
```

### Examples

```
python3 main.py -mode knn -train train3.txt -test test3.txt -k 7 -d e2 -unitw True
```

```
python3 main.py -min -tol 0.001 -i input3.txt
``` 

## Command line flags
 
Below are the list of command-line flags required and accepted by this project.

```

```

## Author

Kumar Prasun (kp2692)