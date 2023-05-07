# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:14:28 2023

@author: Justus
"""

while(1):
    import math
    def schnittHoehe(radius, winkel):
        h = radius*(1-math.cos(math.radians(abs(winkel))))
        return h
    
    def teilVolumen(radius, winkel):
        h = schnittHoehe(radius, winkel)
        if h == radius:
            return (2*math.pi/3)*pow(radius,3)
        elif h == 2*radius:
            return (4*math.pi/3)*pow(radius,3)
        else:
            return math.pi/3*pow(h,2)*(3*radius-h)
    
    def mantelFlaeche(radius, winkel):
        h = schnittHoehe(radius, winkel)
        if h == radius:
            return 2*math.pi*pow(radius,2)
        elif h == 2*radius:
            return 4*math.pi*pow(radius,2)
        else:
            return 2*math.pi*radius*h
    
    print("Aufgabe 1\nTeilvolumen und Mantelfläche von einem Kreis berechnen\nEingabe Radius: ")
    
    eingabe = input()
    
    try:
        radius = float(eingabe)
    except:
        print("Falsches Format!")
        exit()
        
    print("Eingabe Winkel: ")
    
    eingabe = input()
    
    try:
        winkel = float(eingabe)
        if winkel > 180:
            print("Winkel zu groß!")
            exit()
        
    except:
        print("Falsches Format!")
        exit()
    
    oberesVolumen = teilVolumen(radius, winkel)
    unteresVolumen = (4*math.pi/3)*pow(radius,3) - teilVolumen(radius, winkel)
    mFlaeche = mantelFlaeche(radius, winkel)
    
    print("oberes Teilvolumen:\t\t", oberesVolumen.__round__(4), " m³")
    print("unteres Teilvolumen:\t\t", unteresVolumen.__round__(4), " m³")
    print("Flächeninhalt der Mantelfläche: ", mFlaeche.__round__(4), " m²\n\n\n\n")




