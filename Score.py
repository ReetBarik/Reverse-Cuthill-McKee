# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:03:55 2020

@author: reetb
"""

import numpy as np
import math


def print_Scores(filename):
    
    edgelist = np.genfromtxt(filename)

    edgeCount = len(edgelist)
    
    differenceList = [int(x) for x in abs(np.diff(edgelist))]
    expected = [math.pow(x,2) for x in differenceList]
    
    print('Minimum gap          :  ', "{0:.6f}".format(np.min(differenceList)))
    print('Average gap          :  ', "{0:.6f}".format(np.average(differenceList)))
    print('Maximum gap          :  ', "{0:.6f}".format(np.max(differenceList)))
    print('Total (sum) gap score:  ', "{0:.6f}".format(np.sum(differenceList)))
    print('Expected value of X^2:  ', "{0:.6f}".format(np.sum(expected) / edgeCount))
    print('Variance is          :  ', "{0:.6f}".format(np.var(differenceList)))
    print('Standard deviation   :  ', "{0:.6f}".format(np.std(differenceList)))
    print('*******************************************')
    
    differenceList = [math.log10(x) for x in differenceList]
    expected = [math.pow(x,2) for x in differenceList]
    
    print('Minimum log gap      :  ', "{0:.6f}".format(np.min(differenceList)))
    print('Average log gap      :  ', "{0:.6f}".format(np.average(differenceList)))
    print('Maximum log gap      :  ', "{0:.6f}".format(np.max(differenceList)))
    print('Total (sum) gap score:  ', "{0:.6f}".format(np.sum(differenceList)))
    print('Expected value of X^2:  ', "{0:.6f}".format(np.sum(expected) / edgeCount))
    print('Variance is          :  ', "{0:.6f}".format(np.var(differenceList)))
    print('Standard deviation   :  ', "{0:.6f}".format(np.std(differenceList)))
    print('*******************************************')    
    
    
def scores(before, after, order):
    
    edgelist = np.genfromtxt(before)

    vertexCount = order
    edgeCount = len(edgelist)
    
    print('*******************************************')
    print('General Graph: Characteristics :')
    print('*******************************************')
    
    print('Number of vertices   :  ', vertexCount)
    print('Number of edges      :  ', edgeCount)
    print('*******************************************')
    print('\n')
    
    print('*******************************************')
    print('Before Reverse Cuthill-McKee')
    print('*******************************************')
    print_Scores(before)
    print('\n')
    
    print('*******************************************')
    print('After Reverse Cuthill-McKee')
    print('*******************************************')
    print_Scores(after)
