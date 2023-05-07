# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:16:12 2023

@author: Justus
"""

import numpy as np

def create(rows, *cols):
    if cols:
        cols = int(cols[0])
    else:
        cols = rows
    m = np.random.randint(2, size = (rows, cols), dtype = int)
    return m

def neighbourCount(liste ,rows ,cols):
    neighbors = 0
    maxRows, maxCols = liste.shape
    for i in range(3):
        if (rows-1 >= 0 and rows-1 < maxRows and cols-1+i >= 0 and cols-1+i < maxCols):
            if liste[rows-1][cols-1+i] == 1:
                neighbors += 1
    for i in range(3):
            if i != 1:
                if (rows >= 0 and rows < maxRows and cols-1+i >= 0 and cols-1+i < maxCols):
                    if liste[rows][cols-1+i] == 1:
                        neighbors += 1
    for i in range(3):
        if (rows+1 >= 0 and rows+1 < maxRows and cols-1+i >= 0 and cols-1+i < maxCols):
            if liste[rows+1][cols-1+i] == 1:
                neighbors += 1
    return neighbors

def display(liste):
    dictionary = {0: ' ', 1: '*', 2: ':', 3: '!'}
    for row in liste:
        for num in row:
            print(dictionary.get(num, '?'), end='')
        print()                

def neighbourMap(universe):
    rows, cols = universe.shape
    neighbours = np.copy(universe)
    neighbours = np.zeros(universe.shape, dtype=int)    #chreate matrix of 0
    for r in range(rows):
        for c in range(cols):
            neighbours[r][c] = neighbourCount(universe, r, c)
    return neighbours

def nextGeneration(universe, neighbours):
    nextGen = np.copy(universe)
    
    for pos,val in np.ndenumerate(universe):
        num = neighbours[pos]
        if((val == 1 and num == 2) | (val == 1 and num == 3) | (val == 0 and num == 3)):
            nextGen[pos] = 1
        else:
            nextGen[pos] = 0
        
    neighMap = neighbourMap(universe)
    
    return nextGen, neighMap
        
