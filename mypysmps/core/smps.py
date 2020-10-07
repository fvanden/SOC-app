# -*- coding: utf-8 -*-
#################
import warnings
import datetime as dt

from ..config import get_metadata
from ..util.timetransform import TimeTransform
tt = TimeTransform()
#################

"""
mysmps.core.smps
================

A general particle sizer instrument class
    ParticleSizer
    SMPS

Created on Thu Jul 9 14:37 2020

@author: flovan / fvanden

Revision history:   09.07.2020 - Created
                    10.07.2020 - Addittdions to ParticleSizer class
                    20.07.2020 - Added self.__dict__.update(kwargs)
                        for open ended kwargs addition
                    13.08.2020 - Added Empty
                    18.08.2020 - Added createTimeDate and findSample functions
                    07.10.2020 - add_field added to ParticleSizer


"""
## -------------------------------------------------------------------------- ##


class ParticleSizer(object):
    """
    A class storing particle sizer data
    
    Parameters - required
    ---------------------
    time : dict
        Time of each sample
    date: dict
        Date of each sample
    sample: dict
        Sample number
    data : dict
        Data fields of sample measurements
    diameter : dict
        Diameters for data fields
    
    Parameters - optional
    ---------------------
    temperature : dict
        Temperature of each sample
    pressure : dict
        Pressure for each sample
    relative_humidity : dict
        Relative humidity for each sample
    mean_free_path : dict
        Mean Free Path for each sample
    viscosity : dict
        Gas viscosity for each sample
    scan_time : dict
        Scan duration
    retrace_time : dict
        Retrace duration
    scan_resolution : dict
        Scan resolution
    scans_per_sample : dict
        Number of scans per sample
    aerosol_flow : dict
        Aerosol flow in instrument
    lower_size : dict
        Lower size limit in instrument
    upper_size : dict
        Upper size limit in instrument
    density : dict
        Flow density
    td+05 : dict
        Aerosol delay time
    tf : dict
        Time for aerosol to flow through the sample column of the classifier
    D50 : dict
        Cut point diameter of the impactor.
    median : dict
        Median value of sample
    mean : dict
        Mean value of sample
    geo_mean : dict
        Geometric mean value of sample ?
    mode : dict
        Mode of sample
    geo_std_dev : dict
        Geometric standard deviation of sample?
    total_concentration : dict
        Total concentration of samples
    title : dict
        Title of measurement
    user_name : dict
        User name of instrument operator
    sample_id : dict
        ID of sample
    instrument_id : dict
        ID of instrument
    lab_id : dict
        ID of laboratory
    leak_test_rate : dict
        Leak test and leakage rate
    instrument_errors : dict
        Errors reported by instrument
    comment : dict
        Sample comments   
    
    metadata : dict
        Metadata describing the instrument and data
    pddata : pandas table
        data organised in pandas table
        
    #latitude : dict
        Latitude of the instrument
    #longitude : dict
        Longitude of the instrument
    #altitude : dict
        Altitude of the instrument
    
    
    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    def __init__(self, time, date, sample, data, diameter, metadata, pddata, header, **kwargs):
        self.time = time
        self.date = date
        self.sample = sample
        self.data = data
        self.diameter = diameter
        self.metadata = metadata
        self.pddata = pddata
        self.header = header
        
        self.__dict__.update(kwargs)
    
    def __del__(self):
        pass


    ## ------------------------------------------------------------------ ##
    ## Methods                                                            ##
    ## ------------------------------------------------------------------ ##

    # private:
    
    def createTimeDate(self, dtformat = '%Y.%m.%d %H:%M:%S', output = False):
        """
        Creates a list which combines date and time information
        
        Parameters
        ----------
        dtformat : str
            date time format for output list
            
        output : bool
            if True, the list is returned, otherwise it is stored
            in the class instance
            
        Returns
        -------
        list : list of str
            date and time combined in a single time format
        """
        tdlist = []
        timeformat = self.date['units'] + ' ' + self.time['units']
        for i in range(len(self.date['data'])):
            nd = self.date['data'][i] + ' ' + self.time['data'][i]
            tdlist.append(dt.datetime.strftime(dt.datetime.strptime(nd,timeformat), dtformat))
           
        self.datetime = get_metadata('datetime')
        self.datetime['units'] = dtformat
        self.datetime['data'] = tdlist
        
        if output:
            return tdlist
        
    def findSample(self,sample, dtformat = '%Y.%m.%d %H:%M:%S'):
        """
        Finds the sample index or time
        
        Parameters
        ----------
        sample : int or str
            either an integer (sample number) or a string (date)
            
        dtformat : str
            date time format for output
            
        Returns
        -------
        loc : str or int
            depending on the type of input: the date of the sample
            or the index of the date (or closest date)
        """
        
        if isinstance(sample, int):
            # given sample is an integer, 
            # the date and time for the sample
            # will be returned
            return dt.datetime.strftime(dt.datetime.strptime(self.date['data'][sample] + ' ' + self.time['data'][sample],'%d/%m/%Y %H:%M:%S'), dtformat)
        elif isinstance(sample, str):
            # given sample is a string, 
            # the indice for the given time
            # will be returned
            self.createTimeDate(dtformat = dtformat)
            idx, date = tt.findNearestDate(self.datetime, sample)
            return idx
        else:
            print( ("%s is not a relevant input format"%(type)) )
            pass
        

    def add_field(self, fieldname, data, method = None, metadata = None):
        """
        Adds a new field to ParticleSizer object 

        Parameters
        ----------
        fieldname : str
            name of the field to add
            
        data : list or numpy.ma.core.MaskedArray
            a warning is emitted if the data does not have
            the same dimensions as the data present in the
            ParticleSizer object
        
        method : str
            in case of filtered or adapted data, this allows
            to describe the technique applied if the user
            does not wish to add a whole metadata dictionary
            
        metadata : dict
            a dictionary with metadata for the added field, 
            if None, a dictionary from the default config file 
            is loaded
            
        """
        # check if field already exists in object
        
        if fieldname in self.data['variables']:
            warnings.warn( ("field name %s already exists, field is overwritten...")%(fieldname) )
            
        # get metadata for field
        
        if metadata is None:
            metadata = get_metadata(fieldname)
            if metadata == {}:
                metadata = {'units': '-', 'standard_name': fieldname, 'axis': '-', 'valid_min': None, 'valid_max': None, 'comment': None}
        
        if method is not None:
            metadata['method'] = method
            
        # check if data has the right dimensions
        
        objectshape = self.data[self.data['variables'][0]]['data'].shape
        datashape = data.shape
        
        if datashape == objectshape:
            pass
        elif (datashape[1], datashape[0]) == objectshape:
            # try to match shape
            warnings.warn("field data is translated to match existing field shape")
            data = data.T
        elif datashape[0] == objectshape[1]:
            warnings.warn("only one dimension matches existing field shape: these dimensions are matched")
            data = data.T
        elif datashape[1] == objectshape[0]:
            warnings.warn("only one dimension matches existing field shape: these dimensions are matched")
            data = data.T
        else:
            warnings.warn("field data does not match existing field shape")
        
        metadata['data'] = data
        
        # add new field to object data
        
        self.data[fieldname] = metadata
        self.data['variables'].append(fieldname)                



class SMPS(ParticleSizer):
    """
    A class storing SMPS particle sizer data.
    
    Parameters
    ----------
    inherited from ParticleSizer class
    
    sheath_flow : dict
        Sheath Flow in instrument
    bypass_flow : dict
        Bypass flow in instrument
    low_voltage : dict
        Low voltage value in instrument
    high_voltage : dict
        High voltage value in instrument
    neutralizer_status : dict
        Status of the neutralizer
    
    See Also
    --------
    mysmps.core.read.ParticleSizer
    
    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    def __init__(self,time, date, sample, data, diameter, metadata, pddata,header, **kwargs):
        ParticleSizer.__init__(self, time, date, sample, data, diameter, metadata, pddata,header, **kwargs)
        # other stuff if necessary
        
    def __del__(self):
        pass
    
    ## ------------------------------------------------------------------ ##
    ## Methods                                                            ##
    ## ------------------------------------------------------------------ ##

    # private:
    
class Empty(ParticleSizer):
    """
    An empty class for storing particle sizer data.
    
    Parameters
    ----------
    None : class can be initiated empty
    
    See Also
    --------
    mysmps.core.read.ParticleSizer
    
    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    
    def __init__(self, **kwargs):
        time = get_metadata('time')
        time['data'] = []

        date = get_metadata('date')
        date['data'] = []

        sample = get_metadata('sample')
        sample['data'] = []

        data = {}
        data['variables'] = []

        diameter = get_metadata('diameter')
        diameter['data'] = []

        metadata = {}

        pddata = []

        header = []
        ParticleSizer.__init__(self, time, date, sample, data, diameter, metadata, pddata,header, **kwargs)
        # other stuff if necessary
        
    def __del__(self):
        pass
    
    ## ------------------------------------------------------------------ ##
    ## Methods                                                            ##
    ## ------------------------------------------------------------------ ##

    # private: