import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'epa7658577.settings'
from epa7658577 import settings
from nutr.models import *
import csv
dataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/countries2.csv'), delimiter=',', quotechar='"')
import unicodedata
import re

#################################
# warning: deletes all rows !!! #
#################################
Tag.objects.all().delete()

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

for row in dataReader:
  if row == '\n':
    break
  tag=Tag()
  try:

    # 1) country name
    clone1 = row[0].rstrip()
    print ('1: ',clone1)
    try:
        colon = clone1.index(':',0)
        clone1=clone1[colon+1:]
        print ('clone1: ',clone1)
    except Exception as e: 
        print (e)
    print ('2: ',clone1)
    tag.name=clone1

    # 2) create slug from name (lower case, get rid of special characters, numbers, spaces)
    clone2 = clone1[:]
    print ('3: ',clone2)
    clone2=clone2.lower()
    print ('4: ',clone2)
    clone2 =''.join(e for e in clone2 if e.isalpha())
    clone2 = clone2.replace(' ','')
    clone2 = remove_accents(clone2) #this was working
    print ('5: ',clone2)
    tag.slug = clone2
  except:
    pass
  tag.save()
