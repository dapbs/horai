horai
=====





[![Build Status](https://api.travis-ci.org/dapbs/horai.png)](https://travis-ci.org/dapbs/horai)

`horai` is a Python interface for National Oceanic and Atmospheric Administration's (NOAA) U.S. Temperature and Precipitation Seasonal (long-term) Weather Outlooks (forecasts) which are natively provided as .shp and .kmz files via [Web](http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php) and [FTP](ftp://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/).

In Greek mythology the [Horae or Horai or Hours](https://en.wikipedia.org/wiki/Horae) (Greek "Seasons") were the goddesses of the seasons and the natural portions of time.

## About the NOAA U.S. Temperature and Precipitation Seasonal Weather Outlooks Dataset

NOAA releases forecasts ["on the third Thursday of the month, which varies from as early as the 15th to as late as the 21st, depending on the calendar"](http://origin.cpc.ncep.noaa.gov/products/predictions/schedule.php).
Each month a new ZIP archive is added to the FTP server containing 14 consecutive "leads". The number of each "lead" indicates the number of months into the future for the starting month of the three-month series. As an example, the January 2018 file includes the following leads:

|Lead Number    |Months                 |
|:----------|:---------------------------|
|1 |(February, March, April        |
|2 |March, April, May        |
|3 |April, May, June        |
|... |...        |
|11 |February 2019, April 2019, May 2019       |
|12 |December 2018, January 2019, February 2019       |
|13 |January 2019, April 2019, May 2019       |
|14 |March 2019, April 2019, May 2019       |

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

## References

* [http://www.cpc.ncep.noaa.gov/products/forecasts/](http://www.cpc.ncep.noaa.gov/products/forecasts/)
* [http://www.cpc.ncep.noaa.gov/products/predictions/90day/](http://www.cpc.ncep.noaa.gov/products/predictions/90day/)
* [http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php](http://www.cpc.ncep.noaa.gov/products/GIS/GIS_DATA/us_tempprcpfcst/seasonal.php)
* ftp://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/
