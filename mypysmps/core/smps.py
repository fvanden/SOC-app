# -*- coding: utf-8 -*-
#################

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
                    10.07.2020 - Additions to ParticleSizer class
                    20.07.2020 - Added self.__dict__.update(kwargs)
                        for open ended kwargs addition


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