"""
input:
af-ZA,Afrikaans - South Africa,0x0436,AFK,,,,,
sq-AL,Albanian - Albania,0x041C,SQI,,,,,


output:
    (‘hi-IN', _('Hindi')),
    ('zh-CN', _('Chinese')),
"""
import os
import csv
import unicodedata
import re
import time
import sys

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

#################################################################################################################
dataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/country_codes.csv'), delimiter=',', quotechar='"')
#################################################################################################################
for row in dataReader:
    # 1) e.g. pt-BR
    clone1=row[0][:]

    # 2) e.g. Hindi
    clone2=row[1][:]

    print("    ('"+clone1+"', _('"+clone2+"')),")
