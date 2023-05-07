# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:05:32 2023

@author: karbe
"""
import universe as universe  
import os
import time

clear = lambda: os.system('cls')

uni = universe.create(30,100)
neighbourMap = universe.neighbourMap(uni)
universe.display(uni)

while(1):
     
    time.sleep(0.3)
    uni, neighbourMap = universe.nextGeneration(uni, universe.neighbourMap(uni))
    clear()
    universe.display(uni)