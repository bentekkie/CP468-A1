#%%
from typing import List, Tuple
import calculatepath as lib
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from calculatepath import edgeToString

def drawGraph(nodes : List[Tuple[bool,int,int]]):

    figure(num=None, figsize=(25, 15), dpi=80, facecolor='w', edgecolor='k')
    plt.rcParams['axes.facecolor'] = 'white'


    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from( {tuple(sorted((key,value))) for key,values in lib.adjList.items() for value in values})

    plt.subplot(111)
    plt.tight_layout(pad=5)
    pos = nx.kamada_kawai_layout(G)
    nx.draw(
        G, 
        pos,
        with_labels=True, 
        font_weight='bold',
        font_size=20,
        edgecolors=["#FF0000" if state == lib.start or state == lib.end else '#00FF00' for state in list(G.nodes)],
        labels={state:lib.stateToString(state) for state in nodes},
        node_color=["#00FF00" if state in lib.correct_path else "#00FFFF" for state in list(G.nodes)],
        edge_color=["#00FF00" if tuple(sorted(edge)) in lib.correct_edges else "#000000" for edge in list(G.edges)],
        )
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels={x:edgeToString(x) for x in G.edges}
    )
drawGraph(list(lib.adjList.keys()))
plt.savefig("GraphReachable.png")

drawGraph(list(lib.allStates))
plt.savefig("Graph.png")
#%%
