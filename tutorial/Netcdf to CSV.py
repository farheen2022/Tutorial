#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imdlib as imd
import xarray as xr
import numpy as np
import pandas as pd
from netCDF4 import Dataset
start_yr = 1990 # give starting year from which you want to download/convert data: 1901 ownwards for rainfall, 1951 for tmax and tmin
end_yr = 1990 # give ending year upto which you want to download/convert data
variable = 'rain' # give variable name (rain for rainfall at 0.25 deg, tmax or tmin for rainfall, min or max temperature at 1 deg resolution)
file_format = 'nc' # other option (None), which will assume deafult imd naming convention
file_dir = 'Desktop/' 

data = Dataset('1990.nc')
if variable == 'rain':
    grid_size = 1 # grid spacing in deg
    y_count = 33 # no of grids in y direction
    x_count = 35 # no of grids in x direction
    x = 66.5 # starting longitude taken from control file (.ctl)
    y = 6.5 # starting latitude taken from control file (.ctl)
data
r= data.variables['rf']
rainfall=r[:]

#type(data)
years_no = (end_yr - start_yr) + 1  
day = 0
for yr in range(0,years_no):
    f = open("Desktop/"+str(start_yr+yr)+"_"+str(variable)+".csv",'w')
    if ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 != 0):  # check for leap year
        days = 366
        count = yr + days
    elif ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 == 0) and ((start_yr+yr) % 400 == 0):
        days = 366
        count = yr + days
    else:
        days = 365
        count = yr + days
    
    day = day + days
    f.write("X,Y,")
    for d in range(0, days):
        f.write(str(d+1))
        f.write(",")
    f.write("\n")
    
    for j in range(0, y_count):

        for i in range(0, x_count):

            f.write(str((i * grid_size) + x))
            f.write(",")
            f.write(str((j * grid_size) + y))
            f.write(",")
            time = 0
            for k in range(day-days, day):
                val = rainfall[k,j,i]
                if val == 99.9000015258789 or val == -999:
                    f.write(str(-9999))
                    f.write(",")
                else:
                    f.write(str(val))
                    f.write(",")
            
            f.write("\n")


# In[ ]:




