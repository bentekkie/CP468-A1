#%%
import calculatepath as lib
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(num=None, figsize=(23, 10), dpi=80, facecolor='w', edgecolor='k')

G = nx.Graph()
G.add_nodes_from(lib.adjList.keys())
G.add_edges_from( {tuple(sorted((key,value))) for key,values in lib.adjList.items() for value in values})

plt.subplot(111)
plt.tight_layout(pad=5)
nx.draw_kamada_kawai(
    G, 
    with_labels=True, 
    font_weight='bold',
    font_size=20,
    edgecolors=["#FF0000" if state == lib.start or state == lib.end else '#00FF00' for state in list(G.nodes)],
    labels={state:lib.stateToString(state) for state in lib.adjList.keys()},
    node_color=["#00FF00" if state in lib.correct_path else "#00FFFF" for state in list(G.nodes)],
    edge_color=["#00FF00" if edge in lib.correct_edges else "#000000" for edge in list(G.edges)])
plt.savefig("Graph.png")
#%%
