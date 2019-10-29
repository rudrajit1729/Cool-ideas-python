# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:36:01 2019

@author: RUDRAJIT
"""
#importing libraries
import networkx as nx
import random
import matplotlib.pyplot as plt

#Creating the Graph
G=nx.gnp_random_graph(10,0.5,directed=True)
#visualize
nx.draw(G,with_labels=True)
plt.show()

#initializing points
points=[100 for x in range(G.number_of_nodes())]

#distributing points
def distr_points(points,G):
    nodes=list(G.nodes())
    new_points=[0 for x in range(G.number_of_nodes())]
    for n in nodes:
        out=list(G.out_edges(n))
        if len(out)==0:
            new_points[n]+=points[n]
        else:
            share=points[n]/len(out)
            for (src,tgt) in out:
                new_points[tgt]+=share
    return new_points
    
def keep_distr(points,G):
    for i in range(1000):
    #while(1):363666666666
        new_points=distr_points(points,G)
        #print(new_points)
        points=new_points
        #stop=input("Press q to quit any other button to continue:-")
        #if stop=='q':
        #    break
    return new_points

#New points after distribution
new_points=keep_distr(points,G)
dict_counter={i:(new_points[i]/1000) for i in range(len(new_points))}
#verifying with inbuilt function results
result=nx.pagerank(G)
print(sorted(dict_counter.items(),key=lambda f:f[1]))
print("\n")
print(sorted(result.items(),key=lambda f:f[1]))
