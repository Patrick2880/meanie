meanie
======cd storage/downloads/RimmaP
pip install pystyle
python3 rms.py
Python Implementations of Various Mean Calculations:
* Arithmetic mean (`amgm.py`)
* Arithmetric-Geometric mean (`amgm.py`)
* Geometric mean (`amgm.py`)
* Harmonic mean (`hm.py`)
* Root mean square (`rms.py`)

A bonus `evaluate.py` is included to calculate (given precision and recall):
* F-score (i.e. harmonic mean)
* G-measure (i.e. geometric mean)

***

Usage
------

#### To calculate arithmetic-geometric mean: 

```
$ python amgm.py 1 2 3 4 5
Input: ['1', '2', '3', '4', '5']
arithmetic mean =  3.0
geometric mean =  2.6051710847
arithmetic-geometric mean =  2.79910366264

$ python amgm.py 1 2 3 4 5 6 7 8 9 10
Input: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
arithmetic mean =  5.5
geometric mean =  4.52872868812
arithmetic-geometric mean =  5.00257138023

$ python amgm.py 1.0 3.5 0.12 0.58 8.84
Input: ['1.0', '3.5', '0.12', '0.58', '8.84']
arithmetic mean =  2.808
geometric mean =  1.16580498972
arithmetic-geometric mean =  1.89706388084
```

#### To calculate arithmetic-geometric mean using a tab/space delimited file:

Sample input file (`test.txt`):

```
1 2 3 4 5
1.0 3.5 0.12 0.58 8.84
```
bash/shell loop:

```
$ while read line; do python amgm.py $line; done < test.txt
```

Example:

```
$ echo -e "1 2 3 4 5\n1.0 3.5 0.12 0.58 8.84" > test.txt
$ cat test.txt
1 2 3 4 5
1.0 3.5 0.12 0.58 8.84
$ ls
amgm.py   README.md   test.txt
$ while read line; do python amgm.py $line; done < test.txt
Input: ['1', '2', '3', '4', '5']
arithmetic mean =  3.0
geometric mean =  2.6051710847
arithmetic-geometric mean =  2.79910366264
Input: ['1.0', '3.5', '0.12', '0.58', '8.84']
arithmetic mean =  2.808
geometric mean =  1.16580498972
arithmetic-geometric mean =  1.89706388084
```


#### To calculate harmonic mean:
```
$ python hm.py 1 2 3 4 5
Input: ['1', '2', '3', '4', '5']
harmonic mean =  2.1897810219
```

#### To calculate root mean square:
```
$ python rms.py 1 2 3 4 5
Input: ['1', '2', '3', '4', '5']
root mean square=  3.31662479036
```

***

Evaluation Usage
----------------

#### To calculate F-score:
```
$ python evaluate.py fscore 98.453 32.23
precision: 98.453 	recall: 32.23
fscore = 48.5624019957
```

#### To calculate G-measure:
```
$ python evaluate.py gmeasure 98.453 32.23
precision: 98.453 	recall: 32.23
gmeasure = 56.3306327854
```


