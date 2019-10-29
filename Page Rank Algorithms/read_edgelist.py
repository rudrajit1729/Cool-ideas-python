import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist(e"path/pagerank.txt",create_using=nx.DiGraph(),nodetype=int)
nx.draw(G,with_labels=True)
plt.show()