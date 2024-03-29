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
#ataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/azerbaijan2.csv'), delimiter=',', quotechar='"')
dataReader = csv.reader(open('/app/azerbaijan2.csv'), delimiter=',', quotechar='"')
#################################################################################################################
for row in dataReader:
  poc=POC()
  try:
    # 1) name
    clone1=row[1][:]+','+row[2][:]+' '+row[0][:]
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
    clone2 = row[1][:]+row[2][:]
    print('6:', clone2)
    clone2=clone2.lower().rstrip()
    print('7:', clone2)
    clone2 =''.join(e for e in clone2 if e.isalpha())
    print('8a:', clone2)
    #tring  = unicode(string, "utf-8")
    #tring = unidecode(string)
    #lone2 = remove_accents(clone2)
    print('8b:', clone2)
    poc.slug = clone2

    # 3) if name is 'Vi Duc Hoi', image.name should be 'Vi_Duc_Hoi.jpg'
    clone3 = row[1][:]+row[2][:]
    print('8c:', clone3)
    clone3=clone3.lstrip().rstrip()
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
    clone4='Azerbaijan' 
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
        poc.link = 'http://theantimedia.org/the-list-of-political-prisoners-the-azerbaijani-government-wants-hidden/'
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
    """
    try:
        print('32b: ',type(row[3][:]))
        list2.append(row[3][:])
    except:
        print('32g: ',list2)
    s = ''.join(list2)  
    """
    print('32h: ',row[3][:])
    poc.description = row[3][:]
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
