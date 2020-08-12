# -*- coding: utf-8 -*-
#################
import os
import numpy as np
import pandas as pd
import csv
from csv import reader

from .csv_read import read_aim_csv
#################

"""
mysmps.io.txt_read
==================

Functions for reading of csv files:
    read_aim_txt

Created on Thu Jul 24 11:22 2020

@author: flovan / fvanden

Revision history:   24.07.2020 - Created


"""

def read_aim_txt(filename, fileorg = 'AIM', **kwargs):
    """
    Reads SMPS data from a csv file generated by AIM software
    
    Parameters
    ----------
    filename : str
        path and name of file to read
        
    fileorg : str
        different file organisations can be found in the default_config
        for new filetypes add mappings here and specify the filetype
        
    kwargs : 
        metadata, dict : user defined metadata - DEFAULT: taken from file
        header, list : user defined header - DEFAULT: taken from file
        delimiter, str : user defined delimiter - DEFAULT: taken from file
        
    Returns
    -------
    smps : smps
        mysmps.core.smps object
    """
    # rename file into csv file
    
    pre, ext = os.path.splitext(filename)
    newfilename = pre + '.csv'
    os.rename(filename, newfilename)    
    
    # pass to csv reader
    
    SMPS = read_aim_csv(newfilename, fileorg, encoding = 'iso8859_15', **kwargs)
    
    return SMPS
    
    
    