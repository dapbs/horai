# horai
Horai US Long-term Seasonal Weather Forecast

In Greek mythology the Horae or Horai or Hours (Greek "Seasons") were the goddesses of the seasons and the natural portions of time.
Source: https://en.wikipedia.org/wiki/Horae


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
