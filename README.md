meanie
======

Python Implementations of Various Mean Calculations


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
