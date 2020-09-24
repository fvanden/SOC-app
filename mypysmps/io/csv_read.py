# -*- coding: utf-8 -*-
#################
import numpy as np
import pandas as pd
import csv
from csv import reader

from ..core.smps import SMPS
from ..config import get_metadata, get_instrument_header
from .read_aux import smps_file_to_config, opc_file_to_config
#################

"""
mysmps.io.csv_read
==================

Functions for reading of csv files:
    read_aim_csv

Created on Thu Jul 9 15:02 2020

@author: flovan / fvanden

Revision history:   09.07.2020 - Created
                    15.07.2020 - added metadata from config
                    20.07.2020 - completed with file_to_config variables
                    27.07.2020 - reading issues resolved for txt file

"""

def read_aim_csv(filename, fileorg = 'AIM', **kwargs):
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
    
    imetadata = kwargs.get("metadata", None)
    iheader = kwargs.get("header", None)
    delimiter = kwargs.get("delimiter", None)
    encoding = kwargs.get("encoding", None)
    
    with open(filename, encoding = encoding, newline='') as csvfile:
        # get dialect from file
        try:
            dialect = csv.Sniffer().sniff(csvfile.read(2048), delimiters=',:.; ')
            delimiter = dialect.delimiter
        except:
            delimiter = ','
            
    datastart = False
    metadata = []
    data = []
    # open file in read mode
    
    try:
        with open(filename, encoding = encoding, newline='') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj, delimiter=delimiter)
            # Iterate over each r'Start Time'ow in the csv using reader object
            # read until "Sample #" is detected, or 100 iterations have passed
            for i, row in enumerate(csv_reader):
                if datastart is True:
                    # put all below "Sample #" in data
                    data.append(row)
                elif row[0] == "Sample #":
                    #"Sample #" row is header
                    header = row
                    datastart = True
                    header_row = i
                else:
                    # put all above "Sample #" in metadata
                    metadata.append(row)
    except UnicodeDecodeError: # try reading with different encoding
        with open(filename, encoding = 'iso8859_15', newline='') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj, delimiter=delimiter)
            # Iterate over each r'Start Time'ow in the csv using reader object
            # read until "Sample #" is detected, or 100 iterations have passed
            for i, row in enumerate(csv_reader):
                if datastart is True:
                    # put all below "Sample #" in data
                    data.append(row)
                elif row[0] == "Sample #":
                    #"Sample #" row is header
                    header = row
                    datastart = True
                    header_row = i
                else:
                    # put all above "Sample #" in metadata
                    metadata.append(row)
                
    # organise data in dict
    
    datadict = {}
    for hname in header:
        datadict[hname] = []

    for row in range(0,len(data)):
        for column in range(0,len(data[row])):
            datadict[header[column]].append(data[row][column])
            
    # also organise data in pandas dataframe (TEMPORARY??)
    try:
        pddata = pd.read_table(filename, skiprows=int(np.floor(header_row/2)), delimiter=delimiter, header=int(np.floor(header_row/2))+1, encoding = encoding)
    except UnicodeDecodeError: # try reading with different encoding
        pddata = pd.read_table(filename, skiprows=int(np.floor(header_row/2)), delimiter=delimiter, header=int(np.floor(header_row/2))+1, encoding = 'iso8859_15')
        
    # organise metadata in dict
    
    variables = []
    values = []
    for metadat in metadata:
        for i in range(0, len(metadat)):
            if not metadat[i].strip():
                pass
            else:
                if i % 2:
                    values.append(metadat[i])
                else:
                    variables.append(metadat[i])
                    
    metadatadict = {}
    for v,variable in enumerate(variables):
        metadatadict[variable] = values[v]
        
    # if metadata are given in kwargs they are appended 
    # to the metadata here
    if type(imetadata) is dict:
        metadatadict.update(imetadata)
        
                    
    # header were given in kwargs and it is a list
    # it is replaced here. If header is True, False or None, 
    # the header read from the file is used
    if type(iheader) is list:
        header = iheader
    
    # read data into configuration metadata
    # create new file_to_config for differently organised files
    # TODO: smart way to identify which file_to_config function is needed
    
    datadict, diameter, date, time, sample,temperature, pressure, relative_humidity, mean_free_path, viscosity, scan_time, retrace_time, scan_resolution, scans_per_sample, sheath_flow, aerosol_flow, bypass_flow, low_voltage, high_voltage, lower_size, upper_size, density, td05, tf, D50, median, mean, geo_mean, mode, geo_std_dev, total_concentration, title, user_name, sample_id, instrument_id, lab_id, leak_test_rate, instrument_errors, comment = smps_file_to_config(datadict, metadatadict, header,fileorg = fileorg)
    
    
    # write to SMPS

    return SMPS(time, date, sample, datadict, diameter,metadatadict, pddata, header, temperature = temperature, pressure= pressure, relative_humidity=relative_humidity, mean_free_path=mean_free_path, viscosity=viscosity, scan_time=scan_time, retrace_time=retrace_time, scan_resolution=scan_resolution, scans_per_sample=scans_per_sample, sheath_flow=sheath_flow, aerosol_flow=aerosol_flow, bypass_flow=bypass_flow, low_voltage=low_voltage, high_voltage=high_voltage, lower_size=lower_size, upper_size=upper_size, density=density, td05=td05, tf=tf, D50=D50, median=median, mean=mean, geo_mean=geo_mean, mode=mode, geo_std_dev=geo_std_dev, total_concentration=total_concentration, title=title, user_name=user_name, sample_id=sample_id, instrument_id = instrument_id, lab_id=lab_id, leak_test_rate=leak_test_rate, instrument_errors=instrument_errors, comment=comment)

    

def read_opc_csv(filename, fileorg = 'OPC', **kwargs):
    """
    Reads OPC data from a csv file
    
    Parameters
    ----------
    filename : str
        path and name of file to read
        
    fileorg : str
        different file organisations can be found in the default_config
        for new filetypes add mappings here and specify the filetype
        
    kwargs : 
        metadata, dict : user defined metadata - DEFAULT: taken from file
        header, list : user defined header - DEFAULT: taken from mypysmps.default_config file
        delimiter, str : user defined delimiter - DEFAULT: taken from file
        
    Returns
    -------
    smps : smps
        mysmps.core.smps object
    """
    
    header = get_instrument_header('OPC')
    
    metadata = kwargs.get("metadata", None)
    header = kwargs.get("header", header)
    delimiter = kwargs.get("delimiter", None)
    encoding = kwargs.get("encoding", None)
    
    with open(filename, encoding = encoding, newline='') as csvfile:
        # get dialect from file
        try:
            dialect = csv.Sniffer().sniff(csvfile.read(2048), delimiters=',:.; ')
            delimiter = dialect.delimiter
        except:
            delimiter = ';'
            
    data = []
    # open file in read mode
    
    try:
        with open(filename, encoding = encoding, newline='') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj, delimiter=delimiter)
            # Iterate over each line in the csv using reader object
            for i, row in enumerate(csv_reader):    
                data.append(row)
    except UnicodeDecodeError: # try reading with different encoding
        with open(filename, encoding = 'iso8859_15', newline='') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj, delimiter=delimiter)
             # Iterate over each line in the csv using reader object
            for i, row in enumerate(csv_reader):
                data.append(row)
                
    # organise data in dict
    
    datadict = {}
    for hname in header:
        datadict[hname] = []

    for row in range(0,len(data)):
        for column in range(0,len(data[row])):
            datadict[header[column]].append(data[row][column])
            
    return opc_file_to_config(datadict, metadata, header)