from .noaa import NOAA
from .utils import AddMonths
from shapely.geometry import shape, Point
import urllib
import io
import shapefile
from zipfile import ZipFile
import re
import datetime


class SeasonalForecast:
    def __init__(self, weather_provider='noaa', forecast_type = 'temp', forecast_date = None):

        assert weather_provider in ['noaa','weather']
        self.weather_provider = weather_provider
        self.forecast_date = forecast_date
        self.forecast_type = forecast_type

    def get_noaa_data(self):
        latest_file_url = NOAA(forecast_type = self.forecast_type, forecast_date = self.forecast_date).get_latest_file_url()
        url = latest_file_url[0]
        start_date = latest_file_url[1]
        end_date = latest_file_url[2]
        response = urllib.request.urlopen(url).read()
        noaa_files = ZipFile(io.BytesIO(response))
        list_of_shps = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.shp')])
        list_of_shx = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.shx')])
        list_of_dbf = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.dbf')])
        shape_data = []
        lead = []
        for shpname, shxname, dbfname in zip(list_of_shps, list_of_shx, list_of_dbf):
            #Retrieve correct lead order from shapefile name
            lead.append(re.findall(r'\d+', shpname))
            shape_data.append(shapefile.Reader(shp  = io.BytesIO(noaa_files.read(shpname)),
                                                 shx  = io.BytesIO(noaa_files.read(shxname)),
                                                 dbf  = io.BytesIO(noaa_files.read(dbfname))))
        return shape_data,start_date,end_date,lead

    def get_forecast(self, lon, lat):
        noaa_data = self.get_noaa_data()
        weather_data = noaa_data[0]
        start_date = noaa_data[1]
        end_date = noaa_data[2]
        lead = noaa_data[3]
        for item in lead:
            if item[0]==1:
                print("%s %s %s" % (item[0], start_date,str(AddMonths(start_date,1))))
                continue
            elif item[0]==2:
                print("%s %s %s" % (item[0], start_date,str(AddMonths(start_date,3))))
                continue
            else:
                print("%s %s %s" % (item[0], str(AddMonths(start_date,(int(item[0])-2)*3)), str(AddMonths(start_date,(int(item[0])-1)*3))))
        point = Point(lon, lat)
        records = []
        for p in weather_data:
            for sh in range(len(p.shapes())):
                polygon = shape(p.shapes()[sh])
                record = p.records()[sh]
                if polygon.contains(point):
                    records.append([start_date,end_date,record])
        print(lead)
        print(records)
        return [start_date, end_date, lead, records]
