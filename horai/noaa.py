# -*- coding: utf-8 -*-

from ftplib import FTP, all_errors
import tempfile
from .utils import get_file_date


HOSTNAME = 'ftp.cpc.ncep.noaa.gov'
FILE_DIRECTORY = '/GIS/us_tempprcpfcst/'

class NOAA:
    def __init__(self, forecast_type = 'temp', forecast_date=None):
        '''
        Gets seasonal forecast by type
        1: temp will get the tempreature (defualt)
        2: percp will get percp
        '''
        assert forecast_type in ['temp', 'prcp']
        self.forecast_type  = forecast_type
        self.forecast_date  = forecast_date

    def get_latest_file(self):
        filname_pattern = 'seas' + self.forecast_type + '_*'
        with FTP(HOSTNAME) as ftp:
            try:
                ftp.login()
                ftp.cwd(FILE_DIRECTORY)
                file_date = max([get_file_date(fl) for fl in ftp.nlst(filname_pattern)])
                setattr(self, 'file_date', file_date)
                latest_file_name = self.forecast_type + '_' + str(file_date) + '.zip'
                setattr(self, 'latest_file_name', latest_file_name)
                temp_file = tempfile.TemporaryFile()
                file_binary = ftp.retrbinary(f'RETR {latest_file_name}', temp_file.write)
            except all_errors as e:
                print('FTP error:', e)
        return temp_file
