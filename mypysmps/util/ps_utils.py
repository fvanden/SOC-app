# -*- coding: utf-8 -*-
#################
import numpy as np
import datetime as dt
import copy

from .timetransform import TimeTransform
tt = TimeTransform()
#################

"""
mysmps.util.stack_ps
==================

Functions for working with particle sizer instances
    

Created on Tue Sep 22 13:56 2020

@author: flovan / fvanden

Revision history:   22.09.2020 - Created
                               - stack_ps added
                    23.09.2020 - stacking finished, added fill_time to stack_ps 
                
"""

def stack_ps(ps1, ps2, keep_unique = False, fill_time = False):
    """
    Combine two particle sizer instances into one.
    
    Parameters
    ----------
    ps1 : ParticleSizer
        mypysmps.core.smps.ParticleSizer object
        
    ps2 : ParticleSizer
        mypysmps.core.smps.ParticleSizer object
        
    keep_unique : bool
        if set to True, attributes which are present in
        one instance but not in the other are kept, if
        False, only attributes common to both instances
        are preserved
        
    fill_time : bool
        if set to True, a time gap between the two 
        particle sizer instances is filled with NaNs
        
        
    Returns
    -------
    new_ps : ParticleSizer
        mypysmps.core.smps.ParticleSizer object with
        data from both input objects
    """
    # create deepcopies to avoid changing original instances
    
    ps1 = copy.deepcopy(ps1)
    ps2 = copy.deepcopy(ps2)
    
    # create datetime information in PS instances
    
    try:
        _ = getattr(ps1, "datetime")
    except AttributeError:
        ps1.createTimeDate()
        
    try: 
        _ = getattr(ps2, "datetime")
    except AttributeError:
        ps2.createTimeDate()
        
    # check time resolutions
    res1 = (dt.datetime.strptime(ps1.datetime['data'][1], ps1.datetime['units']) - dt.datetime.strptime(ps1.datetime['data'][0], ps1.datetime['units'])).seconds
    res2 = (dt.datetime.strptime(ps2.datetime['data'][1], ps2.datetime['units']) - dt.datetime.strptime(ps2.datetime['data'][0], ps2.datetime['units'])).seconds
    
    if abs(res1-res2) > 60:
        print( ("warning: resolutions differ %d seconds")%(abs(res1-res2)) )
         
    # check if ps1 is "older" than ps2
    
    reversed_order = False
    cut = None
    
    if dt.datetime.strptime(ps1.datetime['data'][-1], ps1.datetime['units']) < dt.datetime.strptime(ps2.datetime['data'][0], ps2.datetime['units']):
        # ps2 starts after ps1 ends
        timediff = (dt.datetime.strptime(ps2.datetime['data'][0], ps2.datetime['units']) - dt.datetime.strptime(ps1.datetime['data'][-1], ps1.datetime['units'])).seconds
    elif dt.datetime.strptime(ps2.datetime['data'][-1], ps2.datetime['units']) < dt.datetime.strptime(ps1.datetime['data'][0], ps1.datetime['units']):
        # ps1 starts after ps2 ends (user has inadvertently switched the order of the instances)
        reversed_order = True
        timediff = (dt.datetime.strptime(ps1.datetime['data'][0], ps1.datetime['units']) - dt.datetime.strptime(ps2.datetime['data'][-1], ps2.datetime['units'])).seconds
    else:
        # yikes! The particle sizer instances have overlapping data
        # it is assumed that ps2 data replaces ps1 data starting 
        # from the overlapping time
        cut, cutdate = tt.findNearestDate(ps1.datetime['data'], ps2.datetime['data'][0])   
        fill_time = False
        
    print(timediff, 1.5*res1)
    # check if filling is required
    if fill_time is True:
        # check time difference
        if reversed_order:
        # ps1 starts after ps2 ends
            if timediff > 1.5*res2:
            # the time gap between two instances has to be
            #  larger than twice the normal resolution
                numdates = int(np.ceil(timediff/res2))
                base = dt.datetime.strptime(ps1.datetime['data'][0], ps1.datetime['units'])
                date_list = [base - dt.timedelta(seconds=res2*x) for x in range(numdates)]
                date_list = date_list[1:] # because numdates starts at 0, first date on date_list is the same as the startdate from the second instance
                datetimelist = [dt.datetime.strftime(dl, ps2.datetime['units']) for dl in date_list]
                ps2.datetime['data'] = np.append(ps2.datetime['data'], datetimelist)
                timelist =  [dt.datetime.strftime(dl, ps2.time['units']) for dl in date_list]
                ps2.time['data'] = np.append(ps2.time['data'], timelist)
                datelist = [dt.datetime.strftime(dl, ps2.date['units']) for dl in date_list]
                ps2.date['data'] = np.append(ps2.date['data'], datelist)
            else:
                fill_time = False
        else:
            if timediff > 1.5*res1:
            # the time gap between two instances has to be
            #  larger than twice the normal resolution
                numdates = int(np.ceil(timediff/res1))
                base = dt.datetime.strptime(ps2.datetime['data'][0], ps2.datetime['units'])
                date_list = [base - dt.timedelta(seconds=res1*x) for x in range(numdates)]
                date_list = date_list[1:] # because numdates starts at 0, first date on date_list is the same as the startdate from the second instance
                ps1.datetime['data'] = np.append(ps1.datetime['data'], date_list)
                datetimelist = [dt.datetime.strftime(dl, ps1.datetime['units']) for dl in date_list]
                ps1.datetime['data'] = np.append(ps1.datetime['data'], datetimelist)
                timelist =  [dt.datetime.strftime(dl, ps1.time['units']) for dl in date_list]
                ps1.time['data'] = np.append(ps1.time['data'], timelist)
                datelist = [dt.datetime.strftime(dl, ps1.date['units']) for dl in date_list]
                ps1.date['data'] = np.append(ps1.date['data'], datelist)
            else:
                fill_time = False
        
        
    # check which attributes are similar in both instances
    if reversed_order:
        # ps1 starts after ps2 ends
        new_ps = copy.deepcopy(ps2)
        for attribute in ps1.__dict__.keys():
            if attribute in ps2.__dict__.keys():
                afield = getattr(new_ps, attribute)
                if attribute == 'diameter':
                    st11, st12, st21, st22, diamlist = check_diameters(ps1.diameter['data'], ps2.diameter['data'])
                              
                    for var in new_ps.data['variables']:
                        if fill_time is True:
                            add = np.ma.zeros((ps2.data[var]['data'].shape[0],len(date_list))) 
                            add[:] = np.nan
                            newdata = np.append(ps2.data[var]['data'],add,axis=1)
                            ps2.data[var]['data'] = newdata
                            
                        sh1 = ps1.data[var]['data'].shape
                        sh2 = ps2.data[var]['data'].shape
                        newfields = (len(diamlist) ,sh1[1] + sh2[1])
                        new_field = np.ma.zeros(newfields)
                        new_field[:] = np.ma.masked
                        
                        new_field[st21:st22, 0:ps2.data[var]['data'][:,:cut].shape[1]] = ps2.data[var]['data'][:,:cut]
                        new_field[st11:st12, ps2.data[var]['data'][:,:cut].shape[1]:] = ps1.data[var]['data']
                        
                        new_ps.data[var]['data'] = new_field
                        
                    afield['data'] = diamlist
                    
                elif attribute == 'data':
                    # data has been appended with diameters
                    pass
                else:
                    try:
                        field_ps2 = getattr(ps2, attribute)
                        field_ps1 = getattr(ps1, attribute)
                    except TypeError:
                        if attribute == 'header':
                            pass
                        else:
                            print( ("Could not append %s attribute")%(attribute) )
                    try:
                        data_ps2 = field_ps2['data']
                        data_ps1 = field_ps1['data']
                        afield['data'] = np.append(data_ps2[:cut], data_ps1)
                    except:
                        print( ("Could not append %s attribute")%(attribute) )
                   
            else:
                if keep_unique:
                    newattribute = getattr(ps1,attribute)
                    newattribute['time'] = ps1['datetime']['data']
                    setattr(new_ps, attribute, newattribute)
                else:
                    pass
        if keep_unique is False:
            # get rid of attributes which were in ps2 but not in ps1
            for attribute in ps2.__dict__.keys():
                if attribute in ps1.__dict__.keys():
                    pass
                else:
                    delattr(new_ps, attribute)
            
            
    else:
        # ps2 starts after ps1 ends
        new_ps = copy.deepcopy(ps1)
        for attribute in ps2.__dict__.keys():
            if attribute in ps1.__dict__.keys():
                afield = getattr(new_ps, attribute)
                if attribute == 'diameter':
                    st11, st12, st21, st22, diamlist = check_diameters(ps1.diameter['data'], ps2.diameter['data'])
                              
                    for var in new_ps.data['variables']:
                        if fill_time is True:
                            add = np.ma.zeros((ps1.data[var]['data'].shape[0],len(date_list))) 
                            add[:] = np.nan
                            newdata = np.append(ps1.data[var]['data'],add,axis=1)
                            ps1.data[var]['data'] = newdata
                            
                        sh1 = ps1.data[var]['data'].shape
                        sh2 = ps2.data[var]['data'].shape
                        newfields = (len(diamlist) ,sh1[1] + sh2[1])
                        new_field = np.ma.zeros(newfields)
                        new_field[:] = np.ma.masked
                        
                        new_field[st11:st12, 0:ps1.data[var]['data'][:,:cut].shape[1]] = ps1.data[var]['data'][:,:cut]
                        new_field[st21:st22, ps1.data[var]['data'][:,:cut].shape[1]:] = ps2.data[var]['data']
                        
                        new_ps.data[var]['data'] = new_field
                        
                    afield['data'] = diamlist
                    
                elif attribute == 'data':
                    # data has been appended with diameters
                    pass
                else:
                    try:
                        field_ps2 = getattr(ps2, attribute)
                        field_ps1 = getattr(ps1, attribute)
                    except TypeError:
                        if attribute == 'header':
                            pass
                        else:
                            print( ("Could not append %s attribute")%(attribute) )
                    try:
                        data_ps2 = field_ps2['data']
                        data_ps1 = field_ps1['data']
                        afield['data'] = np.append(data_ps1[:cut], data_ps2)
                    except:
                        print( ("Could not append %s attribute")%(attribute) )
                    
            else:
                if keep_unique:
                    newattribute = getattr(ps2,attribute)
                    newattribute['time'] = ps2['datetime']['data']
                    setattr(new_ps, attribute,newattribute)
                else:
                    pass
        if keep_unique is False:
            # get rid of attributes which were in ps2 but not in ps1
            for attribute in ps1.__dict__.keys():
                if attribute in ps2.__dict__.keys():
                    pass
                else:
                    delattr(new_ps, attribute)
                    
    print(fill_time)
    
    return new_ps

def check_diameters(diameter1, diameter2):
    """
    """
    
    """
    nlist1 = []
    nlist2 = []
    olist = []
    
    for i in range(0, len(diameter1)):
        if diameter1[i] in diameter2:
            olist.append(diameter1[i])
        else:
            nlist2.append(diameter1[i])

    for i in range(0, len(diameter2)):
        if diameter2[i] in diameter1:
            olist.append(diameter2[i])
        else:
            nlist1.append(diameter2[i])
            
    """
    diamlist = np.append(diameter1, diameter2)
    diamlist.sort()
    diamlist = np.unique(diamlist)
    
    st11 = abs(diamlist - diameter1[0]).argmin()
    st12 = abs(diamlist - diameter1[-1]).argmin()+1
    st21 = abs(diamlist - diameter2[0]).argmin()
    st22 = abs(diamlist - diameter2[-1]).argmin()+1
    
    if st12 >= len(diamlist):
        st12 = None
    if st22 >= len(diamlist):
        st22 = None
            
    return st11, st12, st21, st22, diamlist