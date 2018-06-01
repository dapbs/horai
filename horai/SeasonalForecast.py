from .noaa import NOAA
from shapely.geometry import shape, Point
import urllib
import io
import shapefile
from zipfile import ZipFile


class SeasonalForecast:
    def __init__(self, weather_provider='noaa', forecast_type = 'temp', forecast_date = None):

        assert weather_provider in ['noaa','weather']
        self.weather_provider = weather_provider
        self.forecast_date = forecast_date
        self.forecast_type = forecast_type

    def get_noaa_data(self):
        url =  NOAA(forecast_type = self.forecast_type, forecast_date = self.forecast_date).get_latest_file_url()
        response = urllib.request.urlopen(url).read()
        noaa_files = ZipFile(io.BytesIO(response))
        list_of_shps = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.shp')])
        list_of_shx = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.shx')])
        list_of_dbf = sorted([fil for fil in noaa_files.namelist() if fil.endswith('.dbf')])
        shape_data = []
        for shpname, shxname, dbfname in zip(list_of_shps, list_of_shx, list_of_dbf):
            shape_data.append(shapefile.Reader(shp  = io.BytesIO(noaa_files.read(shpname)),
                                                 shx  = io.BytesIO(noaa_files.read(shxname)),
                                                 dbf  = io.BytesIO(noaa_files.read(dbfname))))
        return shape_data

    def get_forecast(self, lon, lat):
        weather_data = self.get_noaa_data()
        point = Point(lon, lat)
        records = []
        for p in weather_data:
            for sh in range(len(p.shapes())):
                polygon = shape(p.shapes()[sh])
                record = p.records()[sh]
                if polygon.contains(point):
                    records.append(record)
        return records
