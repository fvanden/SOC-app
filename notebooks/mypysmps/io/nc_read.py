#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################
import netCDF4 as nc

from ..config import get_metadata, _DEFAULT_VARIABLES,  _FIELD_MAPPING, _CONVERSIONS
from ..util.ps_utils import convert_units
from ..util.timetransform import TimeTransform
tt = TimeTransform()
#################

"""
mypysmps.io.nc_read
================

Automatic reading of files by detecting format:
    read_mpl
    
Created on Mon Nov 16 18:56 2020

@author: flovan / fvanden

Revision history:   16.11.2020 - Created
                    



"""
## -------------------------------------------------------------------------- ##

def read_mpl(filename, fileorg, **kwargs):
    """
    Reads MPL data from a netCDF file generated by SigmaMPL software
    
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
        message, bool : if True, warning messages are output - DEFAULT: True
        keepvars, list of str : a number of variables are considered redundant
            and are therefore ignored by the reader. If you want to keep these
            input their netCDF names here
        
        
    Returns
    -------
    smps : smps
        mysmps.core.smps object
    """
    #TODO: put copol etc in fields using meta_group = variable key
    
    # read netCDF file
    datafile = nc.Dataset(filename)
    
    # get kwargs
    metadata = kwargs.get("metadata", None)
    header = kwargs.get('header', list(datafile.variables.keys()))
    message = kwargs.get('message', True)
    keepvars = kwargs.get('keepvars', [])
    
    # get conversions dict if exists
    if fileorg in _CONVERSIONS:
        convdict = _CONVERSIONS[fileorg]
        convvars = list(convdict.keys())
        
    
    redundant = []
    rejected = []
    outdict = {}
    
    for variable in header:
        try:
            filenaming =  _FIELD_MAPPING[fileorg][variable]
        except KeyError:
            if variable in keepvars:
                filenaming = variable
            else:
                redundant.append(variable)
                continue
        outdict[filenaming] = get_metadata(filenaming)
        try:
            if filenaming in convvars:
                outdict[filenaming]['data'] = convert_units(datafile[variable][:], *convdict[filenaming])
            else:
                outdict[filenaming]['data'] = datafile[variable][:]
        except:
            rejected.append(variable)
                
    if message:
        print('Could not read: \n')
        for rej in rejected:
            print(rej)
        print('-------------------------------- \n')
        print('Considered redundant and not read: \n (Use keepvars = ["netcdf_variable_name"] to add anyways)')
        for red in redundant:
            print(red)
        print('-------------------------------- \n')
        print('---- set message = False to suppress message output ----')
    
    return outdict
