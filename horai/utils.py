# -*- coding: utf-8 -*-

def get_file_date(fname: str) -> int:
    return int(fname.split("_")[1].split(".")[0])
