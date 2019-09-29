# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:44:57 2019

@author: RUDRAJIT
"""
import networkx as nx
import matplotlib.pyplot as plt
G=nx.gnp_random_graph(20,0.2)#(node,probability of edges assigned)
nx.draw(G)
plt.show()
