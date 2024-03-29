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
if 'Users' in (os.environ['HOME']):
  dataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/cameroon2.csv'), delimiter=',', quotechar='"')
else:
  dataReader = csv.reader(open('/app/cameroon2.csv'), delimiter=',', quotechar='"')
#################################################################################################################
for row in dataReader:
  poc=POC()
  try:
    # 1) name
    clone1=row[0][:]
    if not clone1:
        raise ValueError('empty name')
    print('1:', clone1)
    clone1=clone1.lstrip().rstrip()
    print('2:', clone1)
    #lone1 = ''.join([i for i in clone1 if not i.isdigit()])
    print('3:', clone1)
    #lone1 =''.join(e for e in clone1 if e.isalpha())
    #lone1 = remove_accents(clone1)
    print('4:', clone1)
    try:
        #lone1 = re.sub(r'\[\]',r'',clone1)
        #lone1 = clone1("][","")
        #lone1 = clone1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
        #lone1 = clone1[:-2]
        print('5:', clone1)
    except:
        pass
    poc.name=clone1

    # 2) create slug from name (lower case, get rid of special characters, numbers, spaces)
    clone2=row[0][:]
    clone2=clone2.lower().rstrip()
    print('7:', clone2)
    #lone2 =''.join(e for e in clone2 if e.isalpha())
    print('8a:', clone2)
    #tring  = unicode(string, "utf-8")
    #tring = unidecode(string)
    #lone2 = remove_accents(clone2)
    print('8b:', clone2)
    poc.slug = clone2

    # 3) if name is 'Vi Duc Hoi', image.name should be 'Vi_Duc_Hoi.jpg'
    clone3=row[0][:]
    print('8c:', clone3)
    #lone3=clone3.lstrip().rstrip()
    print('9:', clone3)
    clone3 = clone3.replace(' ','_')
    #lone3 =''.join(e for e in clone3 if e.isalpha())
    print('10:', clone3)
    clone3.lstrip()
    print('11:', clone3)
    clone3 = ''.join([i for i in clone3 if not i.isdigit()])
    print('12:', clone3)
    try:
        #lone3=filter(lambda ch: ch in "[]", clone3)
        #lone3 = clone3.replace("[","")
        #lone3 = re.sub("\[","", clone3)
        clone3 = clone3.rstrip(']')
        print('13:', clone3)
        clone3 = clone3.rstrip('[')
        print('14:', clone3)
    except:
        pass
    clone3+='.jpg'
    print('15:', clone3)
    clone3 = remove_accents(clone3)
    print('16:', clone3)
    poc.image.name = clone3.decode('utf-8')

    # 4) tag is a foreign key
    clone4='Cameroon' 
    #lone4=clone4.lower()
    #lone4 = clone4.replace('_','')
    print('17:', clone4)
    tag=Tag.objects.get(name=clone4)
    print('18:', tag.name)
    poc.tag=tag
    print('19:')

    # 5) link
    try:
        print('30a')
        poc.link = 'http://www.kamerwaves.com/2016/06/list-of-top-vip-prisoners-former.html'
        print('30b')
    except:
        pass
    

    # 6) created_date
    try:
        print('31a')
        poc.created_date=datetime.date()
        #oc.created_date='2017-8-13'
        print('31b')
    except:
        pass

    # 7)
    try:
        print('32a: ',str(row[1][:]))
        list2=[str(row[1][:])]
        print('32b: ',type(row[2][:]))
        list2.append(' '+row[2][:])
        print('32b2: ',type(row[3][:]))
        list2.append(' '+row[3][:])
        print('32c: ',type(row[4][:]))
        list2.append(' '+row[4][:])
        print('32d: ',type(row[5][:]))
        list2.append(' '+row[5][:])
        print('32e: ',type(row[6][:]))
        list2.append(' '+str(row[6][:]))
        print('32f: ',type(row[7][:]))
        list2.append(' '+str(row[7][:]))
        print('32g: ',type(row[8][:]))
        list2.append(' '+str(row[8][:]))
        print('32f: ',type(row[9][:]))
        list2.append(' '+str(row[9][:]))
        print('32h: ',type(row[10][:]))
        list2.append(' '+str(row[10][:]))
        print('32i: ',type(row[11][:]))
        list2.append(' '+str(row[11][:]))
        print('32j: ',type(row[12][:]))
        list2.append(' '+str(row[12][:]))
        print('32k: ',type(row[13][:]))
        list2.append(' '+str(row[13][:]))
        print('32l: ',type(row[14][:]))
        list2.append(' '+str(row[14][:]))
        print('32m: ',type(row[15][:]))
        list2.append(' '+str(row[15][:]))
        print('32n: ',type(row[16][:]))
        list2.append(' '+str(row[16][:]))
        print('32o: ',type(row[17][:]))
        list2.append(' '+str(row[17][:]))
        print('32p: ',type(row[18][:]))
        list2.append(' '+str(row[18][:]))
        print('32q: ',type(row[19][:]))
        list2.append(' '+str(row[19][:]))
        print('32r: ',type(row[20][:]))
        list2.append(' '+str(row[20][:]))
        print('32s: ',type(row[21][:]))
        list2.append(' '+str(row[21][:]))
        print('32t: ',type(row[22][:]))
        list2.append(' '+str(row[22][:]))
    except:
        print('32y: ',list2)
    s = ''.join(list2)  
    print('32z: ',s)
    poc.description = s
    print('36:')
  except:
    e = sys.exc_info()[0]
    print('Error: ',e)
  try:
    poc.save()
  except:
    e = sys.exc_info()[0]
    print('Error: ',e)
    pass
