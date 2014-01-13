# -*- coding: utf-8 -*-

import math, operator

def arithmetic_mean(x): # x is a list of values.
  """ Returns the arithmetic mean given a list of values. """
  return sum(x)/len(x)

def geometric_mean(x): # x is a list of values
  """ Returns the geometric mean given a list of values. """
  return math.pow(reduce(operator.mul, x, 1), 1/float(len(x)))

def arigeo_mean(x, threshold = 1e-10): # x is a list of values
  arith = arithmetic_mean(x)
  geo = geometric_mean(x)
  while math.fabs(arith - geo) > threshold: 
    [arith,geo] = [(arith + geo) / 2.0, math.sqrt(arith * geo)]
  return arith

def main(means):
  means = map(float,means)
  print "arithmetic mean = ", arithmetic_mean(means)
  print "geometric mean = ", geometric_mean(means)
  print "arithmetic-geometric mean = ", arigeo_mean(means)

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    sys.stderr.write('Usage: python %s mean1 mean2 mean3)' % sys.argv[0])
    sys.exit(1)
  main(sys.argv[1:])
