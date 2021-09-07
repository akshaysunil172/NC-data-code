#!/usr/bin/python3
 
#import cdsapi
import netCDF4
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd
 
 
# Open netCDF4 file
f = netCDF4.Dataset('C:\IIT-Bombay-main\output.nc')
 
# Extract variable
t2m = f.variables['t2m']
 
# Get dimensions assuming 3D: time, latitude, longitude
time_dim, lat_dim, lon_dim = t2m.get_dims()
time_var = f.variables[time_dim.name]
times = num2date(time_var[:], time_var.units)
latitudes = f.variables[lat_dim.name][:]
longitudes = f.variables[lon_dim.name][:]
 
output_dir = './'
 
# =============================== METHOD 1 ============================
# Extract each time as a 2D pandas DataFrame and write it to CSV
# =====================================================================
os.makedirs(output_dir, exist_ok=True)
for i, t in enumerate(times):
    filename = os.path.join(output_dir, f'{t.isoformat()}.csv')
    print(f'Writing time {t} to {filename}')
    df = pd.DataFrame(t2m[i, :, :], index=latitudes, columns=longitudes)
    df.to_csv(filename)
print('Done')
 
