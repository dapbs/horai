horai
=====





[![Build Status](https://api.travis-ci.org/dapbs/horai.png)](https://travis-ci.org/dapbs/horai)

`horai` - pronounced huˈreɪ, as in "Hip, hip... Hooray!" - is a Python interface for National Oceanic and Atmospheric Administration's (NOAA) U.S. Temperature and Precipitation Seasonal (long-term) Weather Outlooks (forecasts) which are natively provided as .shp and .kmz files via [Web](http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php) and [FTP](http://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/).

The focus of this interface is to simplify access to this geographic dataset through Python. It further assists in coverting it to a tabular format for specific Latitude/Longitude pairs.

In Greek mythology the [Horae or Horai or Hours](https://en.wikipedia.org/wiki/Horae) (Greek "Seasons") were the goddesses of the seasons and the natural portions of time.

## Functionality

`horai` retrieves the most current ZIP archive from NOAA's FTP, decompresses it and uses [pyshp](https://github.com/GeospatialPython/pyshp) to read each of the 14 ESRI Shapefiles (.shp). Optionally, a past Year/Month can be specified to retrieve a specific outlook (historical) instance.

[shapely](https://github.com/Toblerity/Shapely) is used to retrieve the outlook values for specific latitude/longitude pairs.

TO-DOs include:
* Geocoding support
* Blended results for political boundaries such as states

## About the NOAA U.S. Temperature and Precipitation Seasonal Weather Outlooks Dataset

NOAA's Climate Prediction Center (CPC) "issues [seasonal outlooks of the probability of deviations from normal temperature and precipitation](http://origin.cpc.ncep.noaa.gov/products/forecasts/month_to_season_outlooks.shtml), for the lower 48 states, for a total of 13 seasons [or "leads], each of which covers a period of 3 adjacent calendar months"
The forecasts are released ["on the third Thursday of the month, which varies from as early as the 15th to as late as the 21st, depending on the calendar"](http://origin.cpc.ncep.noaa.gov/products/predictions/schedule.php).

Each month a new ZIP archive is added to the FTP server containing 14 consecutive "leads". The number of each "lead" indicates the number of months into the future for the starting month of the three-month series. As an example, the January 2018 file includes the following leads:

|Lead Number    |Months                 |
|:----------|:---------------------------|
|1 |February 2018, March 2018, April 2018        |
|2 |March 2018, April 2018, May 2018        |
|3 |April 2018, May 2018, June 2018        |
|... |...        |
|11 |February 2019, April 2019, May 2019       |
|12 |December 2018, January 2019, February 2019       |
|13 |January 2019, April 2019, May 2019       |
|14 |March 2019, April 2019, May 2019       |

The ZIP archive includes a .shp file for each lead which in turn includes a series of polygons indicating the outlook and corresponding probability score for specific U.S. regions. The possible values are as follows:
* Below (B) 33~100%
* Near-Normal (N) 33~100%
* Above (A) 33~100%
* Equal Chances (EC): Equal chances for A, N, B

For additional detail on the forecast format see [long-lead forecast tool discussion and analysis](http://origin.cpc.ncep.noaa.gov/products/predictions/90day/tools.html).

## Installation

Latest and greatest:
```bash
pip install git+https://github.com/dapbs/horai.git
```

## Examples

```python
from horai import SeasonalForecast
import pandas as pd
s = SeasonalForecast(weather_provider='noaa')
df = pd.DataFrame(s.get_forecast(-90.3462912,38.6472162))
```

```
r.fields

#The field definition does not change between "leads"

[('DeletionFlag', 'C', 1, 0),
 ['Fcst_Date', 'D', 8, 0],
 ['Valid_Seas', 'C', 254, 0],
 ['Prob', 'F', 13, 11],
 ['Cat', 'C', 254, 0]]

 r.numRecords
 #The number (and content) of records varies between "leads"

 11

 r.records()

 [[datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 40.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 40.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 40.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 40.0, 'Above'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'Below'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 40.0, 'Below'],
 [datetime.date(2018, 5, 17), 'JAS 2018', 33.0, 'EC']]

 r.bbox
 #As expected, the bounding box for the shapefile is that of the U.S.
[-178.2175983623659, 18.921786345087078, -66.96927125875779, 71.40623539396705]

r.shapeType
#As expected, the shape type for the shapefile is polygon
5 #POLYGON

#Like the number of records, the number (and composition) of shapes varies between "leads"
len(r.shapes())
11
```


## References

* [http://www.cpc.ncep.noaa.gov/products/forecasts/](http://www.cpc.ncep.noaa.gov/products/forecasts/)
* [http://www.cpc.ncep.noaa.gov/products/predictions/90day/](http://www.cpc.ncep.noaa.gov/products/predictions/90day/)
* [http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php](http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php)
* [ftp://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/](http://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/)
* [Shapely](https://github.com/Toblerity/Shapely)
* [pyshp](https://github.com/GeospatialPython/pyshp)
