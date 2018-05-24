
# coding: utf-8

# http://www.cpc.ncep.noaa.gov/products/forecasts/
# http://www.cpc.ncep.noaa.gov/products/predictions/90day/    
# http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php
# ftp://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/

# In[1]:

import shapefile
from shapely.geometry import shape, Point
import ftplib
import zipfile
import pandas as pd
from zipfile import ZipFile
import urllib
import re
import os
import glob


# In[2]:

home = os.getenv('LOCALAPPDATA')


# In[3]:

def noaa_download (file_list):
    ftp_directory = 'ftp://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/'
    try:
        file = urllib.request.URLopener()
        file.retrieve(ftp_directory+file_list[0][0], filename = home+'\\python_horai\\'+file_list[0][0])
        file.close()
    except:
        print('FTP down')
    #try:
        #wget.download(url = ftp_directory+file_list[0][0], out = localappdata+'\\python_horai\\')
    #except:
        #print('FTP down')
    #for i in range(len(file_list)):
        #try:
            #wget.download(ftp_directory+file_list[i][0])
        #except:
            #print('FTP down')
        #time.sleep(20)
    return None


# In[4]:

def noaa_unzip(file_list):
    zip_ref = zipfile.ZipFile(home+'\\python_horai\\'+file_list[0][0], 'r')
    zip_ref.extractall(home+'\\python_horai\\'+file_list[0][0]+'_folder\\')
    zip_ref.close()
    #for i in range(len(file_list)):
        #zip_ref = zipfile.ZipFile(home+'\\python_horai\\'+file_list[i][0], 'r')
        #zip_ref.extractall(home+'\\python_horai\\'+file_list[i][0]+'\\')
        #zip_ref.close()


# In[5]:

def noaa_filenames (filetype):
    data = []
    ftp = ftplib.FTP("ftp.cpc.ncep.noaa.gov")
    ftp.login()
    ftp.cwd('/GIS/us_tempprcpfcst/')
    ftp.dir(data.append)
    ftp.quit()
    file_list = []
    i=0
    while i<len(data):
        data_element = data[i].find(filetype)
        if(data_element!=-1):
            index = data[i].find(filetype)
            filename_length = len(filetype) + 9 # YYYYMM.zip
            filename = data[i][index:index+19]
            date = re.findall('\d+', filename)[0]
            file_list.append([filename,date])
        i+=1
    file_list = sorted(file_list, key=lambda file_list: file_list[1], reverse=True)
    return file_list


# In[6]:

def shpfle(lon, lat):
    shapes=[]
    records=[]
    directory = home+'\\python_horai\\'+file_list[0][0]+'_folder'
    shp_files = list(filter(lambda x: x.endswith('.shp'), os.listdir(directory)))
    result = []
    for i in range(0,len(shp_files)):
        r = shapefile.Reader(home+'\\python_horai\\'+file_list[0][0]+'_folder\\'+shp_files[i])
        shapes = r.shapes()
        records = r.shapeRecords()
        result.append(check(lon,lat,records,shapes))
    return result


# In[7]:

def check(lon, lat,records,shapes):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    result=False
    for i in range(len(shapes)):
        polygon = shape(shapes[i])
        record = records[i].record
        if polygon.contains(point):
            #return polygon.contains(point)
            return record
    #return False


# In[8]:

file_list = noaa_filenames('seasprcp_') #'seastemp_' 'seasprcp_'


# In[9]:

noaa_download(file_list)


# In[10]:

noaa_unzip(file_list)


# In[11]:

pd.DataFrame(shpfle(-90.3462912,38.6472162))

