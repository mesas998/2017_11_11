from nutr.models import *
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'epa7658577.settings'
from epa7658577 import settings
from nutr.models import *
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
#ataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/syria.csv'), delimiter=',', quotechar='"')
dataReader = csv.reader(open('/app/syria.csv'), delimiter=',', quotechar='"')
#################################################################################################################
ctr=0
for row in dataReader:
  ctr+=1
  #f ctr>10:
    #reak
  poc=POC()
  try:
    # 1) name
    poc.name='syria-'+row[0][:]

    # 4) tag is a foreign key
    tag=Tag.objects.get(name='Syria')
    poc.tag=tag

    # 5) link
    poc.link = 'http://www.safmcd.com/martyr/view.php'

    # 6) created_date
    poc.created_date=datetime.date()

  except:
    e = sys.exc_info()[0]
    print('Error: ',e)
  try:
    poc.save()
  except:
    e = sys.exc_info()[0]
    print('Error: ',e)
    pass
