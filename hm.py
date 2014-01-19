# -*- coding: utf-8 -*-

import math

def harmonic_mean(x): # x is a list of values.
  """ Returns the harmonic mean given a list of values. """
  return len(x) / sum([1/i for i in x])

def main(means):
  print "Input:", means
  means = map(float,means)
  print "harmonic mean = ", harmonic_mean(means)

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    sys.stderr.write('Usage: python %s mean1 mean2 mean3 ... \n' % sys.argv[0])
    sys.exit(1)
  main(sys.argv[1:])