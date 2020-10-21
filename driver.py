# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:53:09 2020

@author: reetb
"""

import sys
import networkx as nx
from RCM import reverse_cuthill_mckee
from Score import scores

def main():

    inputGraph = sys.argv[1]    
    G = nx.read_edgelist(inputGraph, nodetype = int)
    
    H = reverse_cuthill_mckee(G)    
    nx.write_edgelist(H, inputGraph + '_RCM.edges', data = False)
    
    scores(inputGraph, inputGraph + '_RCM.edges', G.order())



if __name__ == "__main__":
    main()