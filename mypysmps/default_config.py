"""
Configuration file for the PySMPS Toolkit

The values for a number of PySMPS parameters and the default metadata created
when reading files, correcting fields, etc. is controlled by this single
Python configuration file.

PySMPS configuration can be modified by changing this file, it is recommended
that the user keeps a copy of this original file.

"""

##############################################################################
##############################################################################
# Simple configuration
#
# Adjust the values of the variable (right hand side of the equal sign) in
# this section for an easy method of customizing PySMPS. Do not change the
# variable names (the left hand side of the equal sign). More advanced
# settings are based upon these variables. Most users will find that
# adjusting this section is all that is needed.
##############################################################################
##############################################################################

# The default fill value for masked arrays and _FillValue keys
fill_value = "nan"

# Field names used when reading in particle sizer files, comments in each 
# section provide additional information about the fields.

# Particle Sizer data fields
drop_concentration = 'drop_concentration'
corrected_drop_concentration = 'corrected_drop_concentration'


# End of Simple Configuration section

##############################################################################
##############################################################################
# Advanced Configuration
#
# Most users will not want toAerosol Instrument Manager ® Software make any changes in this section.  For users
# who want a more fine-grained control over Py-ART's configuration this
# section provides access to these controls.  The layout of this section can
# be changed, the only requirement for a valid configuration file is that
# the ALL CAPITALIZED variable must must be present with the formatting
# present in this file.  These required variables are:
#
# FILL_VALUE, DEFAULT_METADATA, FILE_SPECIFIC_METADATA, FIELD_MAPPINGS,
# DEFAULT_FIELD_NAMES
#
# This section makes generous use of the variables in the Simple Configuration
# section, this is not required, but simplifies and enforces uniformity on
# the configuration.
##############################################################################
##############################################################################


##############################################################################
# Parameters
#
# Various parameters used in Py-ART.
##############################################################################

# the default fill value for masked arrays and the _FillValue key
FILL_VALUE = fill_value

# Field names used when reading in Particle Sizer files. The comments in this 
# section provide additional information about the fields in that section.

# data field names
number_concentration = 'number_concentration'
diameter_concentration = 'diameter_concentration'
surface_concentration = 'surface_concentration'
volume_concentration = 'volume_concentration'
mass_concentration = 'mass_concentration'

normalised_number_concentration = 'normalised_number_concentration'
normalised_diameter_concentration = 'normalised_diameter_concentration'
normalised_surface_concentration = 'normalised_surface_concentration'
normalised_volume_concentration = 'normalised_volume_concentration'
normalised_mass_concentration = 'normalised_mass_concentration'

number_percentage_concentration = 'number_percentage_concentration'
diameter_percentage_concentration = 'diameter_percentage_concentration'
surface_percentage_concentration = 'surface_percentage_concentration'
volume_percentage_concentration = 'volume_percentage_concentration'
mass_percentage_concentration = 'mass_percentage_concentration'

number_cumulative_concentration = 'number_cumulative_concentration'
diameter_cumulative_concentration = 'diameter_cumulative_concentration'
surface_cumulative_concentration = 'surface_cumulative_concentration'
volume_cumulative_concentration = 'volume_cumulative_concentration'
mass_cumulative_concentration = 'mass_cumulative_concentration'

number_cumulative_percentage_concentration = 'number_cumulative_percentage_concentration'
diameter_cumulative_percentage_concentration = 'diameter_cumulative_percentage_concentration'
surface_cumulative_percentage_concentration = 'surface_cumulative_percentage_concentration'
volume_cumulative_percentage_concentration = 'volume_cumulative_percentage_concentration'
mass_cumulative_percentage_concentration = 'mass_cumulative_percentage_concentration'

raw_counts = 'raw_counts'

particulate_matter1 = 'particulate_matter1'
particulate_matter2_5 = 'particulate_matter2_5'
particulate_matter10 = 'particulate_matter10'

# instrument field names

date = 'date'
time = 'time'
fix_time = 'fix_time'
datetime = 'datetime'
diameter = 'diameter'
temperature = 'temperature'
pressure = 'pressure'
relative_humidity = 'relative_humidity'
mean_free_path = 'mean_free_path'
viscosity = 'viscosity'
scan_time = 'scan_time'
retrace_time = 'retrace_time'
scan_resolution = 'scan_resolution'
scans_per_sample = 'scans_per_sample'
sheath_flow = 'sheath_flow'
aerosol_flow = 'aerosol_flow'
bypass_flow = 'bypass_flow'
low_voltage ='low_voltage'
high_voltage = 'high_voltage'
lower_size = 'lower_size'
upper_size = 'upper_size' 
density = 'density'
td05 = 'td+05' 
tf = 'tf' 
D50 = 'D50' 
neutralizer_status = 'neutralizer_status'
laser_status = 'laser_status'
MeanToFBin1 = 'MeanToFBin1'
MeanToFBin3 = 'MeanToFBin3'
MeanToFBin5 = 'MeanToFBin5'
MeanToFBin7 = 'MeanToFBin7'
reject_glitch = 'reject_glitch'
reject_long_TOF = 'reject_long_TOF'
reject_ratio = 'reject_ratio'
reject_count_OOR = 'reject_count_OOR'
median = 'median'
mean = 'mean'
geo_mean = 'geo_mean'
mode = 'mode'
geo_std_dev = 'geo_std_dev'
total_concentration = 'total_concentration'
title = 'title'
user_name = 'user_name' 
sample_id = 'sample_id'
instrument_id = 'instrument_id'
lab_id = 'lab_id'
leak_test_rate = 'leak_test_rate'
instrument_errors = 'instrument_errors'
comment = 'comment' 
metadata = 'metadata'
pddata = 'pddata'
latitude = 'latitude'
longitude = 'longitude'
altitude = 'altitude'

# The DEFAULT_FIELD_NAMES controls the field names which are used in the
# correction and retrieval algorithms in PySMPS. The keys of the dictionary
# are "internal" names which cannot change, the values are the field names
# which will be used in the algorithms by default. For best results use the
# names defined by the variables in simple configuration section which are
# also used in the DEFAULT_METADATA and FIELD_MAPPINGS variable. If you
# choose to change a field name the names should also be changed in the
# DEFAULT_METADATA and FIELD_MAPPINGS variable. This is not required but
# highly suggested.

# IF CORRECTED FIELDS ARE ADDED, ALSO ADD THESE HERE

DEFAULT_FIELD_NAMES = {
    # Internal field name (do not change): field name used (can change)
    
    # data field names
    
    'number_concentration' : number_concentration, 
    'diameter_concentration' : diameter_concentration,
    'surface_concentration' : surface_concentration,
    'volume_concentration' : volume_concentration,
    'mass_concentration' : mass_concentration,
    'normalised_number_concentration' : normalised_number_concentration,
    'normalised_diameter_concentration' : normalised_diameter_concentration,
    'normalised_surface_concentration' : normalised_surface_concentration,
    'normalised_volume_concentration' : normalised_volume_concentration,
    'normalised_mass_concentration' : normalised_mass_concentration,
    
    'number_percentage_concentration' : number_percentage_concentration,
    'diameter_percentage_concentration' : diameter_percentage_concentration,
    'surface_percentage_concentration' : surface_percentage_concentration,
    'volume_percentage_concentration' : volume_percentage_concentration,
    'mass_percentage_concentration' : mass_percentage_concentration,
    
    'number_cumulative_concentration' : number_cumulative_concentration,
    'diameter_cumulative_concentration' : diameter_cumulative_concentration,
    'surface_cumulative_concentration' : surface_cumulative_concentration,
    'volume_cumulative_concentration' : volume_cumulative_concentration,
    'mass_cumulative_concentration' : mass_cumulative_concentration,
 
    'number_cumulative_percentage_concentration' : number_cumulative_percentage_concentration,
    'diameter_cumulative_percentage_concentration': diameter_cumulative_percentage_concentration,
    'surface_cumulative_percentage_concentration' : surface_cumulative_percentage_concentration,
    'volume_cumulative_percentage_concentration' : volume_cumulative_percentage_concentration,
    'mass_cumulative_percentage_concentration' : mass_cumulative_percentage_concentration,
    
    'raw_counts' : raw_counts, 
    
    'particulate_matter1' : particulate_matter1,
    'particulate_matter2_5' : particulate_matter2_5,
    'particulate_matter10' : particulate_matter10,

    
    # instrument field names
    'date': date,
    'time': time,
    'fix_time': fix_time,
    'datetime': datetime,
    'diameter': diameter,
    'temperature': temperature,
    'pressure': pressure,
    'relative_humidity': relative_humidity,
    'mean_free_path': mean_free_path,
    'viscosity': viscosity,
    'scan_time': scan_time,
    'retrace_time': retrace_time,
    'scan_resolution': scan_resolution,
    'scans_per_sample': scans_per_sample,
    'sheath_flow': sheath_flow,
    'aerosol_flow': aerosol_flow,
    'bypass_flow': bypass_flow,
    'low_voltage': low_voltage,
    'high_voltage': high_voltage,
    'lower_size': lower_size,
    'upper_size': upper_size,
    'density': density, 
    'td+05': td05, 
    'tf': tf, 
    'D50': D50, 
    'neutralizer_status' : neutralizer_status,
    'laser_status': laser_status,
    'MeanToFBin1': MeanToFBin1,
    'MeanToFBin3': MeanToFBin3,
    'MeanToFBin5': MeanToFBin5,
    'MeanToFBin7': MeanToFBin7,
    'reject_glitch' : reject_glitch,
    'reject_long_TOF': reject_long_TOF,
    'reject_ratio' : reject_ratio,
    'reject_count_OOR' : reject_count_OOR, 
    'median': median,
    'mean': mean,
    'geo_mean': geo_mean,
    'mode': mode,
    'geo_std_dev': geo_std_dev,
    'total_concentration': total_concentration,
    'title': title,
    'user_name': user_name,
    'sample_id': sample_id,
    'instrument_id' : instrument_id ,
    'lab_id' : lab_id,
    'leak_test_rate' : leak_test_rate ,
    'instrument_errors' : instrument_errors ,
    'comment' : comment ,
    'metadata': metadata,
    'pddata': pddata,
    'latitude' : latitude,
    'longitude' : longitude,
    'altitude' : altitude
}


##############################################################################
# Default metadata
#
# The DEFAULT_METADATA dictionary contains dictionaries which provide the
# default radar attribute and field metadata. When reading in a file with
# Py-ART the FILE_SPECIFIC_METADATA variable is first queued for a metadata
# dictionary, if it is not found then the metadata in DEFAULT_METADATA is
# utilized.
##############################################################################


DEFAULT_METADATA = {
    # Metadata for data fields
    number_concentration : { 
            'units': u'dN #/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'number_concentration',
            'long_name': 'particle_number_concentration',
            'axis': u'Concentration (dN #/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Number concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    diameter_concentration : { 
            'units': u'dD mm/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'diameter_concentration',
            'long_name': 'particle_diameter_concentration',
            'axis': u'Concentration (dD mm/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Diameter concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    surface_concentration : { 
            'units': u'dS nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'surface_concentration',
            'long_name': 'particle_surface_concentration',
            'axis': u'Concentration (dS nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Surface concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    volume_concentration : { 
            'units': u'dV nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'volume_concentration',
            'long_name': 'particle_volume_concentration',
            'axis': u'Concentration (dV nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Volume concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    mass_concentration : { 
            'units': u'dM \N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'mass_concentration',
            'long_name': 'particle_mass_concentration',
            'axis': u'Concentration (dM \N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Mass concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    normalised_number_concentration : { 
            'units': u'#/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'normalised_number_concentration',
            'long_name': 'particle_normalised_number_concentration',
            'axis': u'dN/dlogDp (#/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Normalised number concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    normalised_diameter_concentration : { 
            'units': u'mm/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'normalised_diameter_concentration',
            'long_name': 'particle_normalised_diameter_concentration',
            'axis': u'dN/dlogDp (mm/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Normalised diameter concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    normalised_surface_concentration : { 
            'units': u'nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'normalised_surface_concentration',
            'long_name': 'particle_normalised_surface_concentration',
            'axis': u'dN/dlogDp (nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Normalised surface concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    normalised_volume_concentration : { 
            'units': u'nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'normalised_volume_concentration',
            'long_name': 'particle_normalised_volume_concentration',
            'axis': u'dN/dlogDp (nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Normalised volume concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    normalised_mass_concentration : { 
            'units': u'\N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'normalised_mass_concentration',
            'long_name': 'particle_normalised_mass_concentration',
            'axis': u'dN/dlogDp (\N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Normalised mass concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    number_percentage_concentration : { 
            'units': '-',
            'standard_name': 'number_percentage_concentration',
            'long_name': 'particle_number_percentage_concentration',
            'axis': 'Number % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Number percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    diameter_percentage_concentration : { 
            'units': '-',
            'standard_name': 'diameter_percentage_concentration',
            'long_name': 'particle_diameter_percentage_concentration',
            'axis': '% Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Diameter percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    surface_percentage_concentration : { 
            'units': '-',
            'standard_name': 'surface_percentage_concentration',
            'long_name': 'particle_surface_percentage_concentration',
            'axis': 'Surface % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Surface percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    volume_percentage_concentration : { 
            'units': '-',
            'standard_name': 'volume_percentage_concentration',
            'long_name': 'particle_volume_percentage_concentration',
            'axis': 'Volume % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Volume percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    mass_percentage_concentration : { 
            'units': '-',
            'standard_name': 'mass_percentage_concentration',
            'long_name': 'particle_mass_percentage_concentration',
            'axis': 'Mass % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Mass percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    number_cumulative_concentration : { 
            'units': u'#/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'number_cumulative_concentration',
            'long_name': 'particle_number_cumulative_concentration',
            'axis': u'Number Cumulative Concentration (#/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Number cumulative concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
        
    diameter_cumulative_concentration : { 
            'units': u'mm/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'diameter_cumulative_concentration',
            'long_name': 'particle_diameter_cumulative_concentration',
            'axis': u'Cumulative Concentration (mm/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Diameter cumulative concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    surface_cumulative_concentration : { 
            'units': u'nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'surface_cumulative_concentration',
            'long_name': 'particle_surface_cumulative_concentration',
            'axis': u'Surface Cumulative Concentration (nm\N{SUPERSCRIPT TWO}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Surface cumulative concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
        
    volume_cumulative_concentration : { 
            'units': u'nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'volume_cumulative_concentration',
            'long_name': 'particle_volume_cumulative_concentration',
            'axis': u'Volume Cumulative Concentration (nm\N{SUPERSCRIPT THREE}/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Volume cumulative concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
        
    mass_cumulative_concentration : { 
            'units': u'\N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE}',
            'standard_name': 'mass_cumulative_concentration',
            'long_name': 'particle_mass_cumulative_concentration',
            'axis': u'Mass Cumulative Concentration (\N{GREEK SMALL LETTER MU}g/cm\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Mass cumulative concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    number_cumulative_percentage_concentration : { 
            'units': '-',
            'standard_name': 'number_cumulative_percentage_concentration',
            'long_name': 'particle_number_cumulative_percentage_concentration',
            'axis': 'Number Cumulative % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Number cumulative percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    diameter_cumulative_percentage_concentration : { 
            'units': '-',
            'standard_name': 'diameter_cumulative_percentage_concentration',
            'long_name': 'particle_diameter_cumulative_percentage_concentration',
            'axis': 'Cumulative % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Diameter cumulative percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    surface_cumulative_percentage_concentration : { 
            'units': '-',
            'standard_name': 'surface_cumulative_percentage_concentration',
            'long_name': 'particle_surface_cumulative_percentage_concentration',
            'axis': 'Surface Cumulative % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Surface cumulative percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    volume_cumulative_percentage_concentration : { 
            'units': '-',
            'standard_name': 'volume_cumulative_percentage_concentration',
            'long_name': 'particle_volume_cumulative_percentage_concentration',
            'axis': 'Volume Cumulative % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Volume cumulative percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here

    mass_cumulative_percentage_concentration : { 
            'units': '-',
            'standard_name': 'mass_cumulative_percentage_concentration',
            'long_name': 'particle_mass_cumulative_percentage_concentration',
            'axis': 'Mass Cumulative % Concentration (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Mass cumulative percentage concentration from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    raw_counts : { 
            'units': '-',
            'standard_name': 'raw_counts',
            'long_name': 'particle_raw_counts',
            'axis': 'Raw Counts (-)',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Raw counts from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    particulate_matter1 : { 
            'units': 'ug/m3',
            'standard_name': 'particulate_matter1',
            'long_name': 'particulate_matter1um',
            'axis': u'Particulate matter 1 \N{GREEK SMALL LETTER MU}m (\N{GREEK SMALL LETTER MU}g/m\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Particulate matter from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    particulate_matter2_5 : { 
            'units': 'ug/m3',
            'standard_name': 'particulate_matter2_5',
            'long_name': 'particulate_matter2_5um',
            'axis': u'Particulate matter 2.5 \N{GREEK SMALL LETTER MU}m (\N{GREEK SMALL LETTER MU}g/m\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Particulate matter from particle sizer'}, # if calculated by mypysmps, it will say so here
    
    particulate_matter10 : { 
            'units': 'ug/m3',
            'standard_name': 'particulate_matter10',
            'long_name': 'particulate_matter10um',
            'axis': u'Particulate matter 10 \N{GREEK SMALL LETTER MU}m (\N{GREEK SMALL LETTER MU}g/m\N{SUPERSCRIPT THREE})',
            'valid_min': None, 
            'valid_max': None,
            'comment': 'Particulate matter from particle sizer'}, # if calculated by mypysmps, it will say so here
   

    # Metadata for particle sizer attributes. CHECK CF STANDARDS!
    'sample' : {
        'units': '#',
        'standard_name': 'sample_number',
        'long_name': 'Sample #',
        'axis': 'Sample [#]',
        'comment': ('Number of the sample')},
    
    'time': {
        'units': '%H:%M:%S',
        'standard_name': 'time',
        'long_name': 'time_of_sample_measurement',
        'axis': 'Time [GMT]',
        'comment': ('Time at the start of the sample measurement?')},
    
    'fix_time': {
        'units': 'seconds',
        'standard_name': 'fix_time',
        'long_name': 'seconds_since_last_fix',
        'axis': 'Seconds since last fix [s]',
        'comment': ('Seconds since last fix')},
                    
    'date': {
        'units': '%d/%m/%Y',
        'standard_name': 'time',
        'long_name': 'date_of_sample_measurement',
        'axis': 'Date',
        'comment': ('Date at the start of the sample measurement?')},
    
    'datetime': {
        'units': '%Y.%m.%d %H:%M:%S',
        'standard_name': 'time',
        'long_name': 'date_of_sample_measurement',
        'axis': 'Time',
        'comment': ('Date at the start of the sample measurement?')},
    
    'diameter': {
        'units': 'nm',
        'standard_name': 'diameter_midpoint',
        'long_name': 'particle_midpoint_diameter',
        'axis': 'Diameter [nm]',
        'valid_min': 0, # instrument dependant, read from instrument data file
        'valid_max': 10000, # default physical value
        'comment': 'Diameter midpoint'},
    
    'temperature': {
        'units': 'degrees celsius',
        'standard_name': 'temperature',
        'long_name': 'sample_temperature',
        'axis': u'Temperature [\N{DEGREE SIGN}C]',
        'comment': 'Sample temperature'},
    
    'pressure': {
        'units': 'kPa',
        'standard_name': 'sample_pressure',
        'long_name': 'sample_pressure',
        'axis': 'Sample pressure [kPa]',
        'comment': 'Sample pressure'},
    
    'relative_humidity': {
        'units': '%',
        'standard_name': 'relative_humidity',
        'long_name': 'sample_relative_humidity',
        'axis': 'Relative Humidity [%]',
        'comment': 'Sample relative humidity'},
    
    'mean_free_path': {
        'units': 'm',
        'standard_name': 'mean_free_path',
        'long_name': 'mean_free_path',
        'axis': 'Mean Free Path [m]',
        'comment': 'Sample Mean Free Path'},
    
    'viscosity': {
        'units': 'Pa*s',
        'standard_name': 'viscosity',
        'long_name': 'sample_viscosity',
        'axis': 'Viscosity [Pa*s]',
        'comment': 'Sample viscosity'},

    'metadata': {
        'Conventions': 'CF/Radial instrument_parameters',
        'version': '1.3',
        'title': '',
        'institution': '',
        'references': '',
        'source': '',
        'history': '',
        'comment': '',
        'instrument_name': ''},


    # Metadata for particle sizer instrument attributes
    'scan_time': {
        'comments': ('Duration of scan time'),
        'meta_group': 'instrument_parameters',
        'long_name': 'scan_time_duration',
        'units': 's',
        'axis': 'Duration of scan time [s]'},
    
    'retrace_time': {
        'comments': ('Duration of retrace time'),
        'meta_group': 'instrument_parameters',
        'long_name': 'retrace_time_duration',
        'units': 's',
        'axis': 'Duration of retrace time [s]'},
    
    'scan_resolution': {
        'comments': ('resolution of scan'),
        'meta_group': 'instrument_parameters',
        'long_name': 'scan_resolution',
        'units': 'Hz',
        'axis': 'Resolution of scan [Hz]'},
    
    'scans_per_sample': {
        'comments': ('Scans per sample'),
        'meta_group': 'instrument_parameters',
        'long_name': 'scans_per_sample',
        'units': '#',
        'axis': 'Scans per sample [#]'},
    
    'sheath_flow': {
        'comments': ('Sheath flow'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sheath_flow',
        'units': 'L/min',
        'axis': 'Sheath flow [L/min]'},
    
    'aerosol_flow': {
        'comments': ('Aerosol flow'),
        'meta_group': 'instrument_parameters',
        'long_name': 'aerosol_flow',
        'units': 'L/min',
        'axis': 'Aerosol flow [L/min]'},
    
    'bypass_flow': {
        'comments': ('Bypass flow'),
        'meta_group': 'instrument_parameters',
        'long_name': 'bypass_flow',
        'units': 'L/min',
        'axis': 'Bypass flow [L/min]'},
    
    'low_voltage': {
        'comments': ('Low voltage value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'low_voltage_value',
        'units': 'V',
        'axis': 'Low voltage value [V]'},
    
    'high_voltage': {
        'comments': ('High voltage value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'high_voltage_value',
        'units': 'V',
        'axis': 'High voltage value [V]'},
    
    'lower_size': {
        'comments': ('Lower size limit'),
        'meta_group': 'instrument_parameters',
        'long_name': 'lower_size',
        'units': 'mm',
        'axis': 'Lower size limit [mm]'},
    
    'upper_size': {
        'comments': ('Upper size limit'),
        'meta_group': 'instrument_parameters',
        'long_name': 'upper_size',
        'units': 'mm',
        'axis': 'Upper size limit [mm]'},
    
    'density': {
        'comments': ('Density ?'),
        'meta_group': 'instrument_parameters',
        'long_name': 'density',
        'units': 'g/cm3',
        'axis': 'Density [g/cm3]'},
    
    'td+05': {
        'comments': ("Delay time: the time it takes for aerosol to travel from the exit slit of the DMA to the sensing region of the CPC. \n It depends on DMA, CPC, and sample tube length. Adjustments to td can fine-tune size accuracy. See p 108 SMPS manual."),
        'meta_group': 'instrument_parameters',
        'long_name': 'delay_time',
        'units': 's',
        'axis': 'td+05 [s]'},
    
    'tf': {
        'comments': ('Calculated time for the aerosol to flow through the sample column of the classifier.\n The calculation is based on the classifiers sheath air flow rate, the polydisperse aerosol \n flow rate and the geometry of the clasifier. See p 108 SMPS manual.' ),
        'meta_group': 'instrument_parameters',
        'long_name': 'tf',
        'units': 's',
        'axis':'tf [s]'},
    
    'D50': {
        'comments': ('Cut point diameter of the impactor. Diameter at which the penetration efficiency of the impactor is 50%.\n The SMPS algorithm takes this into account and ignores all particles larger than the impactor D50. \n The D50 depends on impactor type, aerosol flow rate, and particle density among other things. See p 108 SMPS manual.'),
        'meta_group': 'instrument_parameters',
        'long_name': 'D50',
        'units': 'nm',
        'axis': 'D50 [nm]'},
    
    'neutralizer_status': {
        'comments': ('neutralizer status: ON/OFF'),
        'meta_group': 'instrument_parameters',
        'long_name': 'neutralizer_status',
        'units': 'binary',
        'axis':'Neutralizer status [ON/OFF]'},
    
    'laser_status': {
        'comments': ('laser status number'),
        'meta_group': 'instrument_parameters',
        'long_name': 'laser_status',
        'units': '#',
        'axis':'Laser status [#]'},
    
    'MeanToFBin1': {
        'comments': ('dynamic fan compensation'),
        'meta_group': 'instrument_parameters',
        'long_name': 'MeanToFBin1',
        'units': 'us',
        'axis':'Dynamic Fan Compensation 1 [us]'},
    
    'MeanToFBin3': {
        'comments': ('dynamic fan compensation'),
        'meta_group': 'instrument_parameters',
        'long_name': 'MeanToFBin3',
        'units': 'us',
        'axis':'Dynamic Fan Compensation 3 [us]'},
    
    'MeanToFBin5': {
        'comments': ('dynamic fan compensation'),
        'meta_group': 'instrument_parameters',
        'long_name': 'MeanToFBin5',
        'units': 'us',
        'axis':'Dynamic Fan Compensation 5 [us]'},
    
    'MeanToFBin7': {
        'comments': ('dynamic fan compensation'),
        'meta_group': 'instrument_parameters',
        'long_name': 'MeanToFBin7',
        'units': 'us',
        'axis':'Dynamic Fan Compensation 7 [us]'},
    
    'reject_glitch' : {
        'comments': ('Electronic noise indication, high values could suggest a problem with the unit or the set up.'),
        'meta_group': 'instrument_parameters',
        'long_name': 'electronic_noise_indication',
        'units': '#',
        'axis':'Electronic noise indication (Glitch) [#]'},
    
    'reject_long_TOF': {
        'comments': ('Timing error indication, high values could suggest a problem with the unit or the set up.'),
        'meta_group': 'instrument_parameters',
        'long_name': 'timing_error_indication',
        'units': '#',
        'axis':'Timing error indication (TOF) [#]'},
    
    'reject_ratio' : {
        'comments': ('Ratio of rejected counts?'),
        'meta_group': 'instrument_parameters',
        'long_name': 'reject_ratio',
        'units': '-',
        'axis':'Reject ratio [-]'},
    
    'reject_count_OOR' : {
        'comments': ('Reject count out of range?'),
        'meta_group': 'instrument_parameters',
        'long_name': 'reject_count_OOR',
        'units': '#',
        'axis':'Reject count out of range [#]'},
    
    'median': {
        'comments': ('sample median value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_median',
        'units': 'nm',
        'axis': 'Sample median value [nm]'},
    
    'mean': {
        'comments': ('sample mean value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_mean',
        'units': 'nm',
        'axis': 'Sample mean value [nm]'},
    
    'geo_mean': {
        'comments': ('sample geo. mean value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_geo_mean',
        'units': 'nm',
        'axis':'Sample Geo mean value [nm]'},
    
    'mode': {
        'comments': ('sample mode value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_mode',
        'units': 'nm',
        'axis': 'Sample mode value [nm]'},
    
    'geo_std_dev': {
        'comments': ('sample geo standard deviation value'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_geo_standard_deviation',
        'units': '-',
        'axis': 'Sample Geo standard deviation [-]'},
    
    'total_concentration': {
        'comments': ('sample total concentration'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_total_concentration',
        'units': '#/cm3',
        'axis': 'Sample total concentration [#/cm3]'},
    
    'title' : {
        'comments': ('title of file'),
        'meta_group': 'instrument_parameters',
        'long_name': 'file_title',
        'units': '-'},
    
    'user_name': {
        'comments': ('user name of instrument operator'),
        'meta_group': 'instrument_parameters',
        'long_name': 'user_name_operator',
        'units': '-'},
    
    'sample_id': {
        'comments': ('sample ID'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_ID',
        'units': '-'},
    
    'instrument_id': {
        'comments': ('instrument ID'),
        'meta_group': 'instrument_parameters',
        'long_name': 'instrument_ID',
        'units': '-'},
    
    'lab_id': {
        'comments': ('lab ID'),
        'meta_group': 'instrument_parameters',
        'long_name': 'lab_ID',
        'units': '-'},
    
    'leak_test_rate': {
        'comments': ('Leak test and leakage rate'),
        'meta_group': 'instrument_parameters',
        'long_name': 'leak_test_and_leakage_rate',
        'units': '-'},
    
    'instrument_errors': {
        'comments': ('instrument errors'),
        'meta_group': 'instrument_parameters',
        'long_name': 'instrument_errors',
        'units': '-'},
    
    'comment': {
        'comments': ('Any sample comments'),
        'meta_group': 'instrument_parameters',
        'long_name': 'sample_comments',
        'units': '-'},

    'pddata': {
        'comments': ('Data organised in pandas'),
        'meta_group': 'data',
        'long_name': 'pandas_data',
        'units': '-'},

    # Metadata for instrument location
    'latitude': {
        'long_name': 'Latitude',
        'standard_name': 'Latitude',
        'units': 'degrees_north'},

    'longitude': {
        'long_name': 'Longitude',
        'standard_name': 'Longitude',
        'units': 'degrees_east'},

    'altitude': {
        'long_name': 'Altitude',
        'standard_name': 'Altitude',
        'units': 'meters',
        'positive': 'up'},


}



##############################################################################
# File specific metadata
#
# These dictionaries define metadata that is to be used only when reading in
# a given type of file.  This metadata is used in place of the
# DEFAULT_METADATA when it is avialable.  The main use of these variable
# is to define field specific data, it is safe to leave some/all of these
# empty if the default metadata is acceptable.
##############################################################################

INSTRUMENT_HEADERS = {
    'OPC' : ["Time(HHMMSS.ms)", "seconds since last time", "Latitude", "Longitude", "Seconds since fix", "bin0", "bin1", "bin2", "bin3", "bin4", "bin5", "bin6", "bin7", "bin8", "bin9", "bin10", "bin11", "bin12", "bin13", "bin14", "bin15", "bin16", "bin17", "bin18", "bin19", "bin20", "bin21", "bin22", "bin23", "MtoFBin1", "MtoFBin3", "MtoFbin5", "MtoFBin7", "SampPrd(s)", "SFR(ml/s)", "T(C)", "RH(%)", "PM_A(ug/m^3)", "PM_B", "PM_C", "#RejectGlitch", "#RejectLongTOF", "#RejectRatio", "#RejectCountOutOfRange", "LaserStatus"]
    }

##############################################################################
# Field name mapping
#
# These dictionaries map file field names or data types to a particle sizer
# field name. These are used to populate the particle sizer.data dictionary 
# during a read in PySMPS. A value of None will not include that field in 
# the ParticleSizer object. These can be over-ridden on a per-read basis 
# using the field_mapping parameter, or using setting the file_field_names 
# parameter to True.
##############################################################################



DEFAULT_VARIABLES = { # units, weights # variable name
    'dw/dlogDp' : { 'Number' : 'normalised_number_concentration',
                    'Diameter' : 'normalised_diameter_concentration',
                    'Surface' : 'normalised_surface_concentration',
                    'Volume' : 'normalised_volume_concentration',
                    'Mass' : 'normalised_mass_concentration'},
    'Concentration (DW)': { 'Number' : 'number_concentration',
                    'Diameter' : 'diameter_concentration',
                    'Surface' : 'surface_concentration',
                    'Volume' : 'volume_concentration',
                    'Mass' : 'mass_concentration'},
    '% Concentration' : { 'Number' : 'number_percentage_concentration',
                    'Diameter' : 'diameter_percentage_concentration',
                    'Surface' : 'surface_percentage_concentration',
                    'Volume' : 'volume_percentage_concentration',
                    'Mass' : 'mass_percentage_concentration'},
    
    'Cumulative Conc.' : { 'Number' : 'number_cumulative_concentration',
                    'Diameter' : 'diameter_cumulative_concentration',
                    'Surface' : 'surface_cumulative_concentration',
                    'Volume' : 'volume_cumulative_concentration',
                    'Mass' : 'mass_cumulative_concentration'},
    
    'Cumulative % Conc.': { 'Number' : 'number_cumulative_percentage_concentration',
                    'Diameter' : 'diameter_cumulative_percentage_concentration',
                    'Surface' : 'surface_cumulative_percentage_concentration',
                    'Volume' : 'volume_cumulative_percentage_concentration',
                    'Mass' : 'mass_cumulative_percentage_concentration'},
    
    'Raw Counts' : {'Number' : 'raw_counts'},
    
}

FIELD_MAPPING = {
    'AIM':{'date':'Date',
           'comment':'Comment',
           'instrument_errors': 'Instrument Errors',
           'leak_test_rate' : 'Leak Test and Leakage Rate',
           'lab_id' : 'Lab ID',
           'instrument_id': 'Instrument ID',
           'sample_id' : 'Sample ID',
           'user_name' : 'User Name',
           'title' : 'Title',
           'total_concentration' : 'Total Conc. (#/cm�)',
           'geo_std_dev' : 'Geo. Std. Dev.', 
           'mode': 'Mode (nm)',
           'geo_mean' : 'Geo. Mean (nm)',
           'mean' : 'Mean (nm)',
           'median' : 'Median (nm)',
           'neutralizer_status' :'Neutralizer Status ',
           'D50' : 'D50 (nm)',
           'tf' : 'tf (s)',
           'td+05' : 'td + 0.5 (s)',
           'density' : 'Density (g/cm�)',
           'upper_size' : 'Upper Size (nm)',
           'lower_size' : 'Lower Size (nm)',
           'high_voltage' : 'High Voltage (V)',
           'low_voltage' : 'Low Voltage (V)',
           'bypass_flow' : 'Bypass Flow (L/min)',
           'aerosol_flow' : 'Aerosol Flow (L/min)',
           'sheath_flow' : 'Sheath Flow (L/min)',
           'scans_per_sample' : 'Scans Per Sample',
           'scan_resolution' : 'Scan Resolution (Hz)',
           'retrace_time' : 'Retrace Time (s)',
           'scan_time' : 'Scan Time (s)',
           'viscosity' : 'Gas Viscosity (Pa*s)',
           'mean_free_path' : 'Mean Free Path (m)',
           'relative_humidity' : 'Relative Humidity (%)',
           'pressure' : 'Sample Pressure (kPa)',
           'temperature' : 'Sample Temp (C)',
           'diameter': 'Diameter Midpoint (nm)',
           'time' : 'Start Time',
           'date' : 'Date'
        
    },
    'AIM_csv':{'date':'Date',
           'comment':'Comment',
           'instrument_errors': 'Instrument Errors',
           'leak_test_rate' : 'Leak Test and Leakage Rate',
           'lab_id' : 'Lab ID',
           'instrument_id': 'Instrument ID',
           'sample_id' : 'Sample ID',
           'user_name' : 'User Name',
           'title' : 'Title',
           'total_concentration' : 'Total Conc. (#/cm³)',
           'geo_std_dev' : 'Geo. Std. Dev.', 
           'mode': 'Mode (nm)',
           'geo_mean' : 'Geo. Mean (nm)',
           'mean' : 'Mean (nm)',
           'median' : 'Median (nm)',
           'neutralizer_status' :'Neutralizer Status ',
           'D50' : 'D50 (nm)',
           'tf' : 'tf (s)',
           'td+05' : 'td + 0.5 (s)',
           'density' : 'Density (g/cm³)',
           'upper_size' : 'Upper Size (nm)',
           'lower_size' : 'Lower Size (nm)',
           'high_voltage' : 'High Voltage (V)',
           'low_voltage' : 'Low Voltage (V)',
           'bypass_flow' : 'Bypass Flow (L/min)',
           'aerosol_flow' : 'Aerosol Flow (L/min)',
           'sheath_flow' : 'Sheath Flow (L/min)',
           'scans_per_sample' : 'Scans Per Sample',
           'scan_resolution' : 'Scan Resolution (Hz)',
           'retrace_time' : 'Retrace Time (s)',
           'scan_time' : 'Scan Time (s)',
           'viscosity' : 'Gas Viscosity (Pa*s)',
           'mean_free_path' : 'Mean Free Path (m)',
           'relative_humidity' : 'Relative Humidity (%)',
           'pressure' : 'Sample Pressure (kPa)',
           'temperature' : 'Sample Temp (C)',
           'diameter': 'Diameter Midpoint (nm)',
           'time' : 'Start Time',
           'date' : 'Date'
        
    },
    'AIM_text':{'date':'Date',
           'comment':'Comment',
           'instrument_errors': 'Instrument Errors',
           'leak_test_rate' : 'Leak Test and Leakage Rate',
           'lab_id' : 'Lab ID',
           'instrument_id': 'Instrument ID',
           'sample_id' : 'Sample ID',
           'user_name' : 'User Name',
           'title' : 'Title',
           'total_concentration' : 'Total Conc. (#/cm\xb3)',
           'geo_std_dev' : 'Geo. Std. Dev.', 
           'mode': 'Mode (nm)',
           'geo_mean' : 'Geo. Mean (nm)',
           'mean' : 'Mean (nm)',
           'median' : 'Median (nm)',
           'neutralizer_status' :'Neutralizer Status ',
           'D50' : 'D50 (nm)',
           'tf' : 'tf (s)',
           'td+05' : 'td + 0.5 (s)',
           'density' : 'Density (g/cm\xb3)',
           'upper_size' : 'Upper Size (nm)',
           'lower_size' : 'Lower Size (nm)',
           'high_voltage' : 'High Voltage (V)',
           'low_voltage' : 'Low Voltage (V)',
           'bypass_flow' : 'Bypass Flow (L/min)',
           'aerosol_flow' : 'Aerosol Flow (L/min)',
           'sheath_flow' : 'Sheath Flow (L/min)',
           'scans_per_sample' : 'Scans Per Sample',
           'scan_resolution' : 'Scan Resolution (Hz)',
           'retrace_time' : 'Retrace Time (s)',
           'scan_time' : 'Scan Time (s)',
           'viscosity' : 'Gas Viscosity (Pa*s)',
           'mean_free_path' : 'Mean Free Path (m)',
           'relative_humidity' : 'Relative Humidity (%)',
           'pressure' : 'Sample Pressure (kPa)',
           'temperature' : 'Sample Temp (C)',
           'diameter': 'Diameter Midpoint (nm)',
           'time' : 'Start Time',
           'date' : 'Date'
        
    },
    'OPC':{'time' : 'Time(HHMMSS.ms)',
           'duration': 'seconds since last time',
           'latitude': 'Latitude',
           'longitude': 'Longitude',
           'fix_time': 'Seconds since fix',
           'MeanToFBin1': 'MtoFBin1',
           'MeanToFBin3': 'MtoFBin3',
           'MeanToFBin5': 'MtoFbin5',
           'MeanToFBin7': 'MtoFBin7',
           'scan_time': 'SampPrd(s)',
           'aerosol_flow': 'SFR(ml/s)', 
           'temperature': 'T(C)',
           'relative_humidity': 'RH(%)',
           'particulate_matter1': 'PM_A(ug/m^3)',
           'particulate_matter2_5': 'PM_B',
           'particulate_matter10': 'PM_C',
           'reject_glitch': '#RejectGlitch',
           'reject_long_TOF': '#RejectLongTOF',
           'reject_ratio': '#RejectRatio',
           'reject_count_OOR': '#RejectCountOutOfRange',
           'laser_status': 'LaserStatus'
    }
}

    
    
    



"""
None
"""



DEFAULT_FIELD_COLORMAP = {
    # field name : colormap
    drop_concentration: 'smps_flo',
 
}

# map each field to a limit or a limit function

DEFAULT_FIELD_LIMITS = {
    # field name : limits
    diameter: (0., 100000.), # set to 100 micrometer (in nm) to accomodate for other particle sizer instruments
    raw_counts: (0,20),
    normalised_number_concentration : (1,10000),#
    total_concentration : (1,10000)
}

##############################################################################
# DMA settings
#
##############################################################################

INSTRUMENT_SETTINGS = {
    'SMPS':{
    'long':{'r2':1.961,
            'r1':0.937,
            'length':44.369
            },
    'nano':{'r2':1.905,
            'r1':0.937,
            'length':4.987}
    }
}

##############################################################################
# Figure settings
#
##############################################################################

DEFAULT_FIGURE_SETTINGS = {
    'histplot':{'size':(20,7)
        },
    'heatplot':{'size':(20,7)
        },
    'timeplot':{'size':(20,7)
        }
}