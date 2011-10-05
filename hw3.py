#! /usr/bin/env python


import numpy as n, itertools as its, math as m

#def getphase(ants,passb,srcs,freq):
ants=n.array([[0,0,0],[1,0,0],[0,1,0],[1,1,0]])
passb=n.array([[1,100],[1,100],[1,100],[1,100]])
srcs=n.array([[1,0,0]])
freq=n.array([range(1,11)])

num_ants=len(ants)
c=3e8
l=c/freq  #gives wavelengthi
passbl=c/passb
combs_ants=list(its.combinations(range(num_ants),2))
blines=[(ants[x[1]]-ants[x[0]]) for x in combs_ants]

s_mag=[m.sqrt(x[0]**2+x[1]**2+x[2]**2) for x in srcs]
s_unit=[x/s_mag[i] for i, x in enumerate(srcs)]
b_dot_s=[[] for x in blines]

for i, x in enumerate(blines):
 for j, k in enumerate(s_unit):
   b_dot_s[i].append(x[0]*k[0]+x[1]*k[1]+x[2]*k[2])

b_dot_s=n.array(b_dot_s)
#pb=[(passbl[x[0]],passbl[x[1]])for x in combs_ants]
#pb_range= [(max([x[0][0],x[1][0]]),min([x[0][1],x[1][1]])) for x in pb]

#l_mod=[[] for x in pb_range]
#
#for i, x in enumerate(pb_range):
# for j, k in enumerate(l):
#  a=[d for d in k if x[1]<=d<=x[0]]
#  l_mod[i].append(a)


d_phase=dict((i,[[] for x in srcs]) for i, x in enumerate(blines))

z=1j
for i, x in enumerate(b_dot_s):
 for j, k in enumerate(l):
  for f, g in enumerate(range(len(x))):
    if len(k[f])!=0:
       p=[n.angle(m.exp((-2*m.pi*z*x[f])/(d))) for d in n.array(k[f])]
       d_phase[i][f]=(p)
       print i,j, x[f],k[f], f, p
    elif len(k[f]) == 0:
       d_phase[i][f].append([])
       print i,j, x[f],k[f], f

#return d_phase
#d_phase=((-2*m.pi*z*b_dot_s)/l)
import IPython.Shell
s = IPython.Shell.IPShellEmbed('')
s()
