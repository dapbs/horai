# -*- coding: utf-8 -*-

import io
import datetime
import io
import shapefile
from zipfile import ZipFile
import urllib


def get_file_date(fname: str) -> int:
    return int(fname.split("_")[1].split(".")[0])

def add_months(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = int(d.year + ((( d.month - 1) + x ) / 12 ))
    return datetime.datetime( newyear, newmonth, d.day)


def sync_downloads(): #sync hashfiles
    pass


def get_noaa_data(url, file_name):
    if not url:
        raise AttributeError
    response = urllib.request.urlopen(url).read()
    with ZipFile(io.BytesIO(response)) as noaa_files:
        list_of_shps = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.shp')])
        shape_data = []
        for shpname in list_of_shps:
            shape_data.append(( str(shpname.split("_")[0]).replace('lead',''),
                                shapefile.Reader(shp  = io.BytesIO(noaa_files.read(shpname))),
                                file_name))
        return shape_data
