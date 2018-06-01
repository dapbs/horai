# -*- coding: utf-8 -*-

import io
import datetime

def get_file_date(fname: str) -> int:
    return int(fname.split("_")[1].split(".")[0])

def AddMonths(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = int(d.year + ((( d.month - 1) + x ) / 12 ))
    return datetime.datetime( newyear, newmonth, d.day)
