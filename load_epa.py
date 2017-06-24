import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'food.settings'
from food import settings
from nutr.models import *
import csv
dataReader = csv.reader(open('/Users/michaelsweeney/food/epa.csv'), delimiter=',', quotechar='"')

for row in dataReader:
  try:
    epacolo=EPAColo()
    epacolo.ffdru=row[0]
    epacolo.fregid=row[1]
    epacolo.fsn=row[2]
    epacolo.lat=row[3]
    epacolo.slt=row[4]
    epacolo.loc=row[5]
    epacolo.county = row[6]
    epacolo.fips = row[7]
    epacolo.usps = row[8]
    epacolo.state = row[9]
    epacolo.country = row[10]
    epacolo.postal = row[11]
    epacolo.ffic = row[12]
    epacolo.fan = row[13]
    epacolo.tribe = row[14]
    epacolo.tln = row[15]
    epacolo.cdn = row[16]
    epacolo.huc = row[17]
    epacolo.region = row[18]
    epacolo.type = row[19]
    epacolo.desc = row[20]
    epacolo.cdate = row[21]
    epacolo.udate = row[22]
    epacolo.mex = row[23]
    epacolo.abbrev = row[24]
    epacolo.eit = row[25]
    epacolo.naics = row[26]
    epacolo.ntext = row[27]
    epacolo.sic = row[28]
    epacolo.sict = row[29]
    epacolo.lati = row[30]
    epacolo.long = row[31]
    epacolo.conv = row[32]
    epacolo.hcmt = row[33]
    epacolo.ham = row[34]
    epacolo.rpn = row[35]
    epacolo.hrdn = row[36]
    epacolo.cdsn = row[37]
    epacolo.cbc = row[38]

    epacolo.save()
  except:
    pass
