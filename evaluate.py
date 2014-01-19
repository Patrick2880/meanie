# -*- coding: utf-8 -*-

from amgm import geometric_mean
from hm import harmonic_mean

def gmeasure(p,r):
  return geometric_mean([p,r])

def fscore(p,r):
  return harmonic_mean([p,r])

def main(inputs):
  option, precision, recall = inputs
  print "precision:", precision, "\trecall:", recall
  print option, '= ', globals()[option](float(precision), float(recall))
  
if __name__ == '__main__':
  import sys
  if len(sys.argv) != 4:
    sys.stderr.write('Usage: python %s fscore|gmeasure precision recall \n' \
                     % sys.argv[0])
    sys.exit(1)
  main(sys.argv[1:])
