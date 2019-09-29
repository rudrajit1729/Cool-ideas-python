# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:30:20 2019

@author: RUDRAJIT
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.barabasi_albert_graph(50,2)

#drawing the graph
nx.draw(G)
plt.show()

#saving the graph
nx.write_gexf(G,"analysis1.gexf")

