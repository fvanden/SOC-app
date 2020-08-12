#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################
import warnings
import sys
import os
#################
"""
mypysmps.smpswidgets.controlPanel
================

Auxiliary functions for interactive plots:
    checkfile

Created on Tue Jul 29 08:50 2020

@author: flovan / fvanden

Revision history:   29.07.2020 - Created


"""
## -------------------------------------------------------------------------- ##


def checkFile(filename):
    """
    """
    if filename.endswith(".txt") or filename.endswith(".csv"):
        return False
        print(filename)
    else:
        print("Please choose a valid filename")
        return True
    
def renewPlot():
    """
    """
    pass

def wchooseFile(directory = "data/"):
    """
    """
    options = [os.path.join(root, name)
             for root, dirs, files in os.walk(directory)
             for name in files
             if name.endswith((".txt", ".csv"))]
    return options

def wread(filename):
    """
    """
    fname, fextension = os.path.splitext(filename)
    
    if fextension == '.txt':
        fileorg = 'AIM_text'
    else:
        fileorg = 'AIM'
        
    SMPS = read(filename, fileorg)
    
    return SMPS
    
