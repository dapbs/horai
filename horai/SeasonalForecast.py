
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


class SeasonalForcast:
    def __init__(self):
        pass




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

def check(lon, lat, records, shapes):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    result = False
    for i in range(len(shapes)):
        polygon = shape(shapes[i])
        record = records[i].record
        if polygon.contains(point):
            #return polygon.contains(point)
            return record
    #return False



pd.DataFrame(shpfle(-90.3462912,38.6472162))
