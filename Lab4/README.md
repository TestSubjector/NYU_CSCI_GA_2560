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

```bash
python3 path/to/main.py -mode knn -train $train_file.txt -test $test_file.txt -k k_value -d e2/manh -unitw True/False
```

For running kmeans, we require an additional centroid flag before entering the centroid value

```bash
python3 path/to/main.py -mode kmeans -data $input_file -d e2/manh -centroids a,b,c d,e,f
```

### Examples

For knn

```bash
python3 main.py -train train2.txt -test test2.txt -k 3 -d manh -unitw False 
```

```bash
python3 main.py -mode knn -train train3.txt -test test3.txt -k 7 -d e2 -unitw True
```

For kmeans

```bash
python3 main.py -mode kmeans -data km1.txt -d e2 -centroids 0,0 200,200 500,500
```

```bash
python3 main.py -mode kmeans -data km2.txt -d manh -centroids 0,0,0 200,200,200 500,500,500
```

## Command line flags

Below are the list of command-line flags required and accepted by this project.

**-mode** : Argument should be `knn` or `kmeans`. Selects the algorithm to run. Default is `knn`.  
**-d** : Argument should be `e2` or `manh`. Selects the distance function to use. Default is `e2`.

### knn specific flags

**-train** : A file containing training data.  
**-test** : A file containing test data.  
**-k** : Argument should be k value to use. Default is `3`.  
**-unitw** : Argument should be `True` or `False`. Decides the voting weights. Default is `False`.  

### kmean specific flags

**-data** : A file containing data to cluster  
**-centroids** : List of centroids for the program. 

## Author

Kumar Prasun (kp2692)