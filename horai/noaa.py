# -*- coding: utf-8 -*-

from ftplib import FTP, all_errors
from .utils import get_file_date


HOSTNAME = 'ftp.cpc.ncep.noaa.gov'
FILE_DIRECTORY = '/GIS/us_tempprcpfcst/'

class NOAA:
    def __init__(self, forecast_type = 'temp', forecast_date = None):
        '''
        Gets seasonal forecast by type
        1: temp will get the tempreature (defualt)
        2: percp will get percp

        Forecast Date = None, will get the latest
        '''
        assert forecast_type in ['temp', 'prcp']
        self.forecast_type  = 'seas' + forecast_type

    def get_latest_file_url(self):
        filname_pattern =  self.forecast_type + '_*'
        with FTP(HOSTNAME) as ftp:
            try:
                ftp.login()
                ftp.cwd(FILE_DIRECTORY)
                if forecast_date:
                    file_date = forecast_date
                else:
                    file_date = max([get_file_date(fl) for fl in ftp.nlst(filname_pattern)])
                setattr(self, 'file_date', file_date)
                file_name = self.forecast_type + '_' + str(file_date) + '.zip'
                setattr(self, 'file_name', file_name)
                file_url = 'ftp://' + HOSTNAME + FILE_DIRECTORY + file_name
            except all_errors as e:
                print('FTP error:', e)
        return file_url
