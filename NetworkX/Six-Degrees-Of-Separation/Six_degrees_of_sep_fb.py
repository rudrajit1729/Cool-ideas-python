# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:28:19 2019

@author: RUDRAJIT
"""

import networkx as nx
import numpy

G=nx.read_edgelist("facebook_combined.txt")
N=list(G.nodes())#list of nodes
spll=[]#shortest path linked list
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between {0} and {1} is {2}".format(u,v,l))
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)
#print("Min spl={0}\nMax length={1}\nAvg spl={2}".format(min_spl,max_spl,avg_spl))

