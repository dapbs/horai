from .noaa import NOAA
from .utils import add_months
from shapely.geometry import shape, Point
import re
import datetime


class SeasonalForecast:
    def __init__(self, weather_provider='noaa', forecast_type = 'temp', forecast_date = None):
        assert weather_provider in ['noaa','weather']
        self.weather_provider = weather_provider
        self.forecast_date = forecast_date
        self.forecast_type = forecast_type

    def get_data(self):
        if self.weather_provider == 'noaa':
            d = NOAA(self.forecast_date).get_noaa_data()
        return d

    def get_forecast(self, lon, lat):
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
