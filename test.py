from horai import SeasonalForecast
import pandas as pd
#s = SeasonalForecast(weather_provider='noaa',forecast_date='201801')
s = SeasonalForecast()
print(pd.DataFrame(s.get_forecast(-90.3462912,38.6472162)))
s = SeasonalForecast(forecast_type='prcp')
print(pd.DataFrame(s.get_forecast(-90.3462912,38.6472162)))
