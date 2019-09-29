# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:09:07 2019

@author: RUDRAJIT
"""
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
l=[1,2,3]
l2=[(1,2),(2,3),(1,3)]
'''
G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)

print(G.nodes())
print(G.edges())
'''
G.add_nodes_from(l)
G.add_edges_from(l2)
nx.draw(G)
plt.show()
