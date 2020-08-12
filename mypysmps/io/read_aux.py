# -*- coding: utf-8 -*-
#################
import numpy as np
import warnings

from ..config import get_metadata, _DEFAULT_VARIABLES,  _FIELD_MAPPING

#################

"""
mysmps.io.read_aux
==================

Auxiliary functions for reading of files:
    file_to_config

Created on Thu Jul 17 11:05 2020

@author: flovan / fvanden

Revision history:   15.07.2020 - Created
                    20.07.2020 - Completed until working version
                    27.07.2020 - Resolved reading issues text files with exceptions
                    

"""

def file_to_config(datadict, metadatadict, header, fileorg = 'AIM', **kwargs):
    """
    Organises data read from file into metadata dictionaries 
    from config
    
    Parameters
    ----------
    datadict : dict 
        dictionary with data read from file
    
    metadatadict : dict
        dictionary with metadata read from file
        
    header : list
        file header
        
    fileorg : str
        organisation of the file
        
    Returns
    -------
    metadatadictionaries : dict
        all of the data and variables in the format specified in the configuration files
    
    
    """
    
    # date and time
    date = get_metadata('date')
    date['data'] = datadict['Date']
    
    time = get_metadata('time')
    time['data'] = datadict['Start Time']
    
    
    # data, sample and diameter variables
    field = {}
    datafield = _DEFAULT_VARIABLES[metadatadict['Units']][metadatadict['Weight']]
    field[datafield] = get_metadata(datafield)
    field['variables'] = [datafield]
    
    sample = get_metadata('sample')
    data = []
    
    if 'Sample #' in header:   # diameters in header columns, samples in rows. Should be adjusted for different readers 
        field['coordinates'] = ['diameter','sample'] 
        diameter = get_metadata('diameter')
        diameterdata = []
        
        for item in header:
            try:
                if isinstance( float(item), float):
                    diameterdata.append(float(item))
                    data.append([float(i) for i in datadict[item]]) 
            except ValueError:
                pass
        diameter['data'] = diameterdata
        field[datafield]['data'] = np.ma.asarray(data)
        sample['data'] = [float(i) for i in datadict['Sample #']]
        
        if 'Upper Size (nm)' in datadict.keys():
            diameter['valid_max'] = np.max( [float(i) for i in datadict['Upper Size (nm)']] )
        if 'Lower Size (nm)' in datadict.keys():
            diameter['valid_min'] = np.max( [float(i) for i in datadict['Lower Size (nm)']] )
        
    else:
        field['coordinates'] = ['sample', 'diameter']
        # TODO
        
    
    variable = 'temperature'
    temperature = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    temperature['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'pressure'
    pressure = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    pressure['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'relative_humidity'
    relative_humidity = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    relative_humidity['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'mean_free_path'
    mean_free_path = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    mean_free_path['data'] = [float(i) for i in datadict[filenaming]] 
    
    variable = 'viscosity'
    viscosity = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    viscosity['data'] = [float(i) for i in datadict[filenaming]] 
    
    variable = 'scan_time'
    scan_time = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    scan_time['data'] =  [float(i) for i in datadict[filenaming]] 
    
    variable = 'retrace_time'
    retrace_time = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    retrace_time['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'scan_resolution'
    scan_resolution = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    scan_resolution['data'] =  [float(i) for i in datadict[filenaming]]
    
    variable = 'scans_per_sample'
    scans_per_sample = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    scans_per_sample['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'sheath_flow'
    sheath_flow = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    sheath_flow['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'aerosol_flow'
    aerosol_flow = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    aerosol_flow['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'bypass_flow'
    bypass_flow = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    bypass_flow['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'low_voltage'
    low_voltage = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    low_voltage['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'high_voltage'
    high_voltage = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    high_voltage['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'lower_size'
    lower_size = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    lower_size['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'upper_size'
    upper_size = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    upper_size['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'density'
    density = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        density['data'] = [float(i) for i in datadict[filenaming]]
    except KeyError:
        if fileorg == 'AIM':
            filenaming = _FIELD_MAPPING['AIM_text'][variable]
            density['data'] = [float(i) for i in datadict[filenaming]]
        elif fileorg == 'AIM_text':
            filenaming = _FIELD_MAPPING['AIM'][variable]
            density['data'] = [float(i) for i in datadict[filenaming]]
        else:
            warnings.warn("If reading fails, try a different file organisation")        
    
    variable = 'td+05'
    td05 = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    td05['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'tf'
    tf = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    tf['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'D50'
    D50 = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    D50['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'neutralizer_status'
    neutralizer_status = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    
    try:
        neutralizer_status['data'] = [float(i) for i in datadict[filenaming]]
    except ValueError:
        neutralizer_status['data'] = datadict[filenaming]
    
    variable = 'median'
    median = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    median['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'mean'
    mean = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    mean['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'geo_mean'
    geo_mean = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    geo_mean['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'mode'
    mode = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    mode['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'geo_std_dev'
    geo_std_dev = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    geo_std_dev['data'] = [float(i) for i in datadict[filenaming]] 
    
    variable = 'total_concentration'
    total_concentration = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        total_concentration['data'] = [float(i) for i in datadict[filenaming]] 
    except KeyError:
        if fileorg == 'AIM':
            filenaming = _FIELD_MAPPING['AIM_text'][variable]
            total_concentration['data'] = [float(i) for i in datadict[filenaming]] 
        elif fileorg == 'AIM_text':
            filenaming = _FIELD_MAPPING['AIM'][variable]
            total_concentration['data'] = [float(i) for i in datadict[filenaming]] 
        else:
            warnings.warn("If reading fails, try a different file organisation") 
    
    variable = 'title'
    title = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    title['data'] = datadict[filenaming]
    
    variable = 'user_name'
    user_name = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    user_name['data'] = datadict[filenaming] 
    
    variable = 'sample_id'
    sample_id = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        sample_id['data'] = [float(i) for i in datadict[filenaming]]
    except ValueError:
        sample_id['data'] = datadict[filenaming]
    
    variable = 'instrument_id'
    instrument_id = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        instrument_id['data'] = datadict[filenaming]
    except ValueError:
        instrument_id['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'lab_id'
    lab_id = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        lab_id['data'] = datadict[filenaming]
    except ValueError:
        lab_id['data'] = [float(i) for i in datadict[filenaming]]
    
    variable = 'leak_test_rate'
    leak_test_rate = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        leak_test_rate['data'] = [float(i) for i in datadict[filenaming]]
    except ValueError:
        leak_test_rate['data'] = datadict[filenaming]
    
    variable = 'instrument_errors'
    instrument_errors = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    try:
        instrument_errors['data'] =  [float(i) for i in datadict[filenaming]]
    except ValueError:
        instrument_errors['data'] =  datadict[filenaming]
    
    variable = 'comment'
    comment = get_metadata(variable)
    filenaming =  _FIELD_MAPPING[fileorg][variable]
    comment['data'] = datadict[filenaming]
    
    return field, diameter, date, time, sample, temperature, pressure, relative_humidity, mean_free_path, viscosity, scan_time, retrace_time, scan_resolution, scans_per_sample, sheath_flow, aerosol_flow, bypass_flow, low_voltage, high_voltage, lower_size, upper_size, density, td05, tf, D50, median, mean, geo_mean, mode, geo_std_dev, total_concentration, title, user_name, sample_id, instrument_id, lab_id, leak_test_rate, instrument_errors, comment