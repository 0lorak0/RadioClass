#! /usr/bin/env python 

##module to perform 1D and 2D convolutions
#definition of a convolution:
# (f * g)(t)= int(f(tau)G(t-tau) dtau)
import numpy as n, pylab as p, sys

f=sys.argv[1]
g=sys.argv[2]





