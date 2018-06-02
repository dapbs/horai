# -*- coding: utf-8 -*-

from ftplib import FTP, all_errors
from .utils import get_file_date, get_noaa_data
import datetime
from collections import namedtuple

HOSTNAME = 'ftp.cpc.ncep.noaa.gov'
FILE_DIRECTORY = '/GIS/us_tempprcpfcst/'

class NOAA:
    def __init__(self, forecast_date = None):
        self.forecast_date = forecast_date

    def _check_for_date(self):
        if datetime.date(self.forecast_date).year < 2012:
            raise NotImplementedError

    def _ftp_file_names(self):
        with FTP(HOSTNAME) as ftp:
            try:
                ftp.login()
                ftp.cwd(FILE_DIRECTORY)
                temp_files = [fl for fl in ftp.nlst('seastemp_*')]
                precp_files = [fl for fl in ftp.nlst('seasprcp_*')]
            except all_errors as e:
                print('FTP error:', e)
        return temp_files, precp_files


    def _get_filenames(self):
        temp_files, precp_files = self._ftp_file_names()
        all_files = temp_files + precp_files
        #tp = namedtuple(typename='str', field_names=['date','file_name'])
        enriched_filenames = [(x, get_file_date(x)) for x in all_files]
        if not self.forecast_date:
            s_date = max([get_file_date(x) for x in all_files])
            noaa_files = [x[0] for x in enriched_filenames if x[1] == s_date]
        else:
            noaa_files = [x[0] for x in enriched_filenames if x[1] >= int(self.forecast_date)]
        return noaa_files

    def get_noaa_data(self):
        all_files = self._get_filenames()
        noaa_data = []
        for url in all_files:
            noaa_data.append(get_noaa_data('http://'+ HOSTNAME + FILE_DIRECTORY + url, url))
        return noaa_data
