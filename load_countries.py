import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'epa7658577.settings'
from epa7658577 import settings
from nutr.models import *
import csv
dataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/countries.csv'), delimiter=',', quotechar='"')

for row in dataReader:
  try:
    poc=POC()
    poc.country=row[0]
    poc.name=row[1]

    poc.save()
  except:
    pass
