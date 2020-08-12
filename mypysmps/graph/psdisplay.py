# -*- coding: utf-8 -*-
#################
import warnings
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as mtick
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.ticker import LogFormatter 
import datetime as dt

from ._cm import _smps_flo
from ..util.mathfuncs import roundup
from ..config import get_figure_settings, _DEFAULT_FIELD_LIMITS
import mypysmps.util.timetransform as timetransform
tt = timetransform.TimeTransform()
#################

"""
mysmps.graph.psdisplay
==================

A general particle sizer display class
    display

Created on Mon Jul 20 13:46 2020
perhaps it would be worthwhile to contact the manufacturer  



@author: flovan / fvanden

Revision history:   20.07.2020 - Created


"""

class PSDisplay(object):
    """
    A class for displaying particle sizer data
    
    Parameters
    ----------
    smps - SMPS
        core.SMPS object to use for creating plots
        
    Attributes
    ----------
        
    """
    ## ------------------------------------------------------------------ ##
    ## Constructors/Destructors                                           ##
    ## ------------------------------------------------------------------ ##
    def __init__(self, smps, **kwargs ):
        self._smps = smps        
        self.__dict__.update(kwargs)
    
    def __del__(self):
        pass


    ## ------------------------------------------------------------------ ##
    ## Plotting methods                                                   ##
    ## ------------------------------------------------------------------ ##

    # private:
    
    def plot(self, field, **kwargs):
        """
        Create a heatmap of particle sizer data
        
        Parameters
        ----------
        field : str
            data field to plot
            
        kwargs:
            indicator
            colorbar
            xlim
            ylim
            clim
            set_time
            time_format
            xlabel
            ylabel
            title
            return_axes
            
            
        See Also
        --------       
        
        """
        # get relevant kwargs
        indperiods = kwargs.get("periods",False)
        
        # get figure settings
        figdict = get_figure_settings('heatplot')
        
        # create figure
        fig, ax = plt.subplots(figsize=figdict['size'])
        
        # get plot data
        plotdata = self._smps.data[field]['data']
        
        # get data coordinates
        coord = self._smps.data['coordinates']
        xcoord = getattr(self._smps, coord[0])
        ycoord = getattr(self._smps, coord[1])
        
        # get relevant kwargs
        indicatorline = kwargs.get("indicator", False)
        
        x = xcoord['data']
        y = ycoord['data']
          
        X, Y = np.meshgrid(x,y)
        
        # get colorbar
        if 'colorbar' in kwargs:
            colorbar = kwargs.get("colorbar")
            cbar = cm.get_cmap(colorbar)
        else:
            # get custom colorbar
            cbar = mcolors.ListedColormap(_smps_flo)
        
        
        # plot data
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            c = plt.pcolormesh(Y,X,plotdata.T, cmap=cbar)
        
        fig.colorbar(c, format=ticker.FuncFormatter(self.fmt))           
        
        # set plot color to black
        ax.set_facecolor('black')
        
        # set axes limits
        xlim = kwargs.get("xlim", None)  
        
        ylim = kwargs.get("ylim", (10**0,7*10**2))
        try:
            len(ylim) # ylim is a tuple
        except TypeError: # ylim is a single value 
            ylim = [10**0, ylim]
        
        clim = kwargs.get("clim", (0.0, 2.0*10**4))
        try:
            len(clim)
        except TypeError: # clim is a single value 
            clim = [0, clim]
        
        # plot periods if True
        
        if indperiods:
            plist = self.find24hourperiods()
            for p in plist:
                self.plotIndicator(ax, [p,p], [ylim[0], ylim[1]],'b--')
                
        # plot indicator line if True
        
        if indicatorline is not False:
            self.plotIndicator(ax, [indicatorline, indicatorline],[ylim[0], ylim[1]],'r--')
            #ax.plot([indicatorline, indicatorline],[ylim[0], ylim[1]],'r--')
                
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("%.3g"))
        
        
        # set axes labels and other
        set_time = kwargs.get("set_time", True)
        if set_time is True:
            datetimes = []
            for i in range(0, len(self._smps.time['data'])):
                datetimes.append( self._smps.date['data'][i] + ' ' + self._smps.time['data'][i] )
            
            x_values = [dt.datetime.strptime(d,"%d/%m/%Y %H:%M:%S") for d in datetimes]
            time_format = kwargs.get("time_format", '%d-%m %H:%M')
            newlabels = [dt.datetime.strftime(d, time_format) for d in x_values]
            #labelnums = [int(item.get_position()[0]) for item in ax.get_xticklabels()]
            labelnums = np.ceil(np.arange(0,roundup(len(newlabels))+1, roundup(len(newlabels))/8))
            labelnums = [int(d) for d in labelnums]
            labels = []

            for i in range(0, len(labelnums)):
                try:
                    labels.append(newlabels[labelnums[i]])
                except IndexError:
                    labels.append(newlabels[-1])
            
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                ax.set_xticks(labelnums)
                ax.set_xticklabels(labels)
                
            #formatter = DateFormatter(time_format)
            #ax.xaxis.set_major_formatter(formatter)
            
        
            xlabel = kwargs.get("xlabel", self._smps.time['axis'])
        else:
            xlabel = kwargs.get("xlabel", ycoord['axis']) 
        
        ylabel = kwargs.get("ylabel", xcoord['axis'])
        
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        if xlim is None:
            add = roundup(len(y))/10
            xlim = [-add, len(y)+add]
        
        # set axes limits
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        plt.clim(clim)
        
        # set title
        title = kwargs.get("title", self._smps.metadata['Sample File'] )
        plt.title(title)
            
        # if return axes is True, return them
        return_axes = kwargs.get("return_axes", False)
        if return_axes is True:
            return fig, ax
        
    
    
    def histogram(self, field, sample= 0, **kwargs):
        """
        Create a histogram plot for the particle sizer
        
        Parameters
        ----------
        field : str
            data field to plot
        sample : int
            sample number to plot
            
        Parameters - optional
        ---------------------
        xlim : tuple of floats
            limits of the x axis
        ylim : tuple of floats
            limits of the y axis
        xlabel : str
            name of x axis
        ylabel : str
            name of y axis    
        add_D50 : bool
            add a D50 impactor line to the plot
        add_boundaries : bool
            add upper and lower boundaries to plot
        add_legend : bool
            add legend to a plot
        D50_linec : str
            colour of D50 line
        boundary_linec : str
            colour of upper and lower boundary lines
        legend_loc : str
            location of thee legend
        return_axes : bool
            returns axes and figure handles
            
        See Also
        --------
        
        """
        # get kwargs     
        xlabel = kwargs.get("xlabel", self._smps.diameter['axis'])
        ylabel = kwargs.get("ylabel", self._smps.data[field]['axis']) 
        addD50 = kwargs.get("add_D50", False)
        addboundaries = kwargs.get("add_boundaries", False)
        addlegend = kwargs.get("add_legend", False)
        D50_linec = kwargs.get("D50_line", 'k--')
        boundary_linec = kwargs.get("boundary_line", 'cyan')
        legend_loc = kwargs.get("legend_loc", 'best') 
        return_axes = kwargs.get("return_axes", False)
        
        
        ylim = kwargs.get("ylim", _DEFAULT_FIELD_LIMITS[field])
        try:
            len(ylim) # ylim is a tuple
        except TypeError: # ylim is a single value 
            ylim = [_DEFAULT_FIELD_LIMITS[field][0], ylim]

        
        xlim = kwargs.get("xlim", [1,1000])
        try:
            len(xlim) # xlim is a tuple
        except TypeError: # xlim is a single value 
            xlim = [1, xlim]
        
        
        # get figure settings
        figdict = get_figure_settings('histplot')
        
        # create figure
        fig, ax = plt.subplots(figsize=figdict['size'])
        
        # get plot data
        plotdata = self._smps.data[field]['data'][:,sample]
        
        # get bins
        bins = self.create_bins()
        
        # take only bin widths
        dwidths = bins[:,2] - bins[:,0]
        
        # create bar plot - take midpoint diameter of bins
        ax.bar(x=bins[:,1], height = plotdata,width = dwidths, color = 'blue', edgecolor = 'white', align = 'edge')
        
        # add extra's if required
        if addD50:
            xval = self._smps.D50['data'][sample]
            ax.plot([xval, xval],[ylim[0], ylim[1]], D50_linec, label = 'D50 impactor')
            ax.text(xval - ((xlim[1] - xlim[0])/3.5), ylim[1] - ((ylim[1] - ylim[0])/30), 'D50 impactor')
        
        if addboundaries:
            xval_lower = self._smps.diameter['valid_min']
            xval_upper = self._smps.diameter['valid_max']
            ax.plot([xval_lower, xval_lower],[ylim[0],ylim[1]], boundary_linec, label = 'lower boundary')
            ax.plot([xval_upper, xval_upper],[ylim[0],ylim[1]], boundary_linec, label = 'upper boundary')
        
            
        # set axes limits
        if ylim is None:
            ylim = [np.nanmin(plotdata), np.nanmax(plotdata)]
        
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        ax.semilogx()
        
        if ylim[1] > 9999:
            ax.xaxis.set_major_formatter(mtick.FormatStrFormatter("%.4g"))
            fmt = mtick.ScalarFormatter()
            fmt.set_powerlimits((0, 1))
            ax.yaxis.set_major_formatter(fmt)
        elif ylim[1] > 999:
            ax.xaxis.set_major_formatter(mtick.FormatStrFormatter("%.3g"))
            fmt = mtick.ScalarFormatter()
            fmt.set_powerlimits((0, 1))
            ax.yaxis.set_major_formatter(fmt)
        else:
            pass

        # set axes names        
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # set title
        title = kwargs.get("title", self._smps.metadata['Sample File'] + '  ' + 'Sample: %d'%(sample+1) )
        plt.title(title)
        
        # add legend if applicable
        if addlegend:
            ax.legend(loc=legend_loc)
        
        # if return axes is True, return them
        if return_axes is True:
            return fig, ax
        
        
        
    def create_bins(self,):
        """
        Creates bins for histogram plot
        
        Parameters
        ----------
        
        See Also
        --------
        
        """
        # create empty matrix
        bins = np.empty((np.asarray(self._smps.diameter['data']).shape[0], 3))
        
        # obtain number of channels per decade
        cpd = float(self._smps.metadata['Channels/Decade'])
        
        # fill bins with NaNs so that bins fail if method fails
        bins.fill(np.NaN)
        
        # fill bins with diameters
        bins[:, 1] = np.asarray(self._smps.diameter['data'])
        bins[0, 0] = self._smps.diameter['valid_min']
        bins[-1, -1] = self._smps.diameter['valid_max']
        
        for i in range(bins.shape[0] - 1):
            bins[i, 2] = round(math.pow(10, np.log10(bins[i, 0]) + 1./cpd), 4)
            bins[i+1, 0] = bins[i, 2]
            
        return bins
    
    def fmt(self,x, pos):
        """
        """
        a, b = '{:.2e}'.format(x).split('e')
        b = int(b)
        return r'${} \times 10^{{{}}}$'.format(a, b)
        
    def plotInfo(self, **kwargs):
        """
        
        """
        other_var = ['aerosol_flow','bypass_flow','sheath_flow','D50','density','geo_mean','low_voltage','high_voltage','mean_free_path','pressure','retrace_time', 'td05','tf','viscosity']
        
        # take in other var if not already present in other values
        for value in kwargs:
            if value in other_var:
                pass
            else:
                other_var.append(value)
             
        # get metadata items
        mydata = self._smps.metadata
        
        # add other items        
        other_dict = {}
        
        for item in other_var:
            itemdat = getattr(self._smps, item)
            other_dict[item +'[' + itemdat['units'] + ']'] = np.mean(itemdat['data'])
            
        mydata.update(other_dict)
        
        # print items
        for key, value in mydata.items():
            line = ['\033[1m' + key + ':' + '\033[0m',  value]
            print('{:>52} | {:<52}'.format(line[0], line[1]) )
            
            
    def dateInfo(self, sample):
        """
        Prints the time and date of a SMPS sample
        
        Parameters
        ----------
        sample : int
            sample number
        
        """
        date = dt.datetime.strftime(dt.datetime.strptime(self._smps.date['data'][sample], '%d/%m/%Y'), '%A, %d %B %Y, ')  +  self._smps.time['data'][sample]
        text = ("Date: " + date)
        print(text)
        
    def plotIndicator(self, ax, xlims, ylims, linec):
        """
        plots and indicator line
        
        Parameters
        ----------
        ax : matplotlib figure axis
            axis of the figure
            
        xlims : tuple
            x limits of indicator line
        
        ylims : tuple
            y limits of indicator line
            
        linec : str
            line type and colour
        """
        ax.plot(xlims,ylims,linec)
        
    def defineIndicator(self, date):
        """
        defines x (and y) position of a date on the plot
        
        Parameters
        ----------
        date : str
            date in '%d-%m-%Y %H:%M:%S' format
            
        """
        pass
    
    def find24hourperiods(self,):
        datetimes = []
        for i in range(0, len(self._smps.time['data'])):
            datetimes.append( self._smps.date['data'][i] + ' ' + self._smps.time['data'][i] )

        times = tt.convertTime(datetimes,'%d/%m/%Y %H:%M:%S','%Y.%m.%d %H:%M:%S')

        indices = []
        for day in np.unique(self._smps.date['data']):
            newtime = tt.convertTime([day + ' 00:00:00'],'%d/%m/%Y %H:%M:%S','%Y.%m.%d %H:%M:%S')
            ind = tt.findNearestDate(times, newtime[0])
            indices.append( ind[0])

        indices = sorted(indices)
        return indices