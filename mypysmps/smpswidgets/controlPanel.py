#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################
from IPython.display import Image, display, Math, Latex, HTML, Javascript
from ipywidgets import widgets, interact, Layout, interactive
import os
import numpy as np
import math
import matplotlib.pyplot as plt

from mypysmps.io.read import read
from mypysmps.graph.psdisplay import PSDisplay
from mypysmps.util.basic import D50, calcC, calcKn, conversion, particleFractions
from mypysmps.smpswidgets.widget_aux import checkFile
#################
"""
mypysmps.smpswidgets.controlPanel
================

Control panel widget and functions for interactive plots:
    cpwidget

Created on Tue Jul 28 17:22 2020

@author: flovan / fvanden

Revision history:   28.07.2020 - Created


"""
## -------------------------------------------------------------------------- ##

def cpwidget(directory = "data/testdata"):
    """
    Creates a control panel widget for interactive plotting of
    SMPS files
    
    Parameters
    ----------
    directory : str
        path where SMPS files are stored
              
    Returns
    -------
    form : widgets.Box 
        widgets box with widgets inside
    
    """
    # read in files and options
    options = ["Choose file ..."]
    for file in os.listdir(directory):
        if file.endswith(".txt") or file.endswith(".csv"):
            options.append(file)
    
    # form layout
    form_item_layout = Layout(
            display='flex',
            flex_flow='row',
            justify_content='space-between'
        )

    filename =  widgets.Dropdown(options= options, value = "LongTerm.csv", description='Filename', layout = form_item_layout)
    
    plottype = widgets.ToggleButtons(
    options=['Heatmap','Histogram'],
    description='Plot type:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Heat map of all samples','Histogram of selected sample'],
)
    maxlen = widgets.interactive_output(readlenfromwidget, {'filename':filename}) 
    
    """
    if smps is None:
        maxlen = 1
        fields = ["no fields"]
        text = "Select a valid data file"
    else:
        maxlen = len(smps.value.sample['data'])
        fields = smps.value.data['variables']
        text = '...reading'
    """
        
    sample = widgets.IntSlider(min=0, max=maxlen, description = 'sample #', layout=form_item_layout)
    sfields = widgets.ToggleButtons(
    options=fields,
    description='Variable:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=fields,
)
    
    outplot =  widgets.interactive_output(createPlot,{'smps':smps, 'sample':sample, 'plottype':plottype}) 

    information = widgets.Box([widgets.Label(value='Information'), widgets.Textarea()], layout=form_item_layout)
    
    form_items = [filename,text, plottype, sfields, sample,information]

    form = widgets.Box(form_items, layout=Layout(
            display='flex',
            flex_flow='column',
            border='solid 2px',
            align_items='stretch',
            width='50%'
        ))
    
    return form

def readlenfromwidget(filename):
    """
    """
    newfilename = os.path.join(os.getcwd(),"data/testdata",filename)
    try:
        smps = read(newfilename)
        maxlen = len(smps.sample['data'])
    except:
        maxlen = 1
        
    return maxlen
        

def createPlot(smps, field, sample, plottype):
    """
    
    """
    if smps is None:
        # get figure settings
        figdict = get_figure_settings('heatplot')
        
        # create figure
        fig, ax = plt.subplots(figsize=figdict['size'])
        
        ax.text(0,0, "ERROR")
    else:
        display = PSDisplay(SMPS)
        if plottype == "Heatmap":
            display.plot()
        elif plottype == "Histogram":
            display.histogram(field, sample = sample)