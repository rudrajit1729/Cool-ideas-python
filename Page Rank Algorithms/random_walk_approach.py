# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:14:25 2019

@author: RUDRAJIT
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()

#picking some random source node as x
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}#counter
#initialization
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[x]+=1#increamenting visit of source node by 1

for i in range(1000000):
    list_n=list(G.neighbors(x))
    if len(list_n)==0:#sink node
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]+=1
    else:
        x=random.choice(list_n)#choose random node from the remaining nodes
        dict_counter[x]+=1

#verifying data with inbuilt functions
p=nx.pagerank(G)
sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))#sorted random walk
print(sorted_p)
print(sorted_rw)
