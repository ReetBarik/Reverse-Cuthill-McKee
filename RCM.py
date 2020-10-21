# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:50:48 2020

@author: reetb
"""

import networkx as nx

def reverse_cuthill_mckee(G):

    nx.set_node_attributes(G, False, "visited")
    nx.set_node_attributes(G, dict(G.degree), "degree")


    reorder = []

    for component in list(nx.connected_components(G)):
    
        frontier = []
        startVertex = sorted(component, key=lambda x: G.nodes[x]["degree"], reverse = False)[0]
        frontier.append(startVertex)
        G.nodes[startVertex]["visited"] = True
        
        while (len(frontier) > 0):
            n = frontier.pop(0)
            reorder.append(n)
            
            for child in sorted(G.neighbors(n), key=lambda x: G.nodes[x]["degree"], reverse=False):
                if (G.nodes[child]["visited"] == False):
                    G.nodes[child]["visited"] = True
                    frontier.append(child)
                
    mapping = {}

    for i in range(len(reorder)):
        mapping[reorder[i]] = i
    
    G = nx.relabel_nodes(G, mapping)

    return G