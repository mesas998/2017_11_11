from nutr.models import *
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'epa7658577.settings'
from epa7658577 import settings
from nutr.models import *
import csv
import unicodedata
import re

#################################
# warning: deletes all rows !!! #
#################################
POC.objects.all().delete()

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

dataReader = csv.reader(open('/Users/michaelsweeney/epa7658577/poc.csv'), delimiter=',', quotechar='"')
for row in dataReader:
  poc=POC()
  try:
    # 1) name
    clone1=row[1][:]
    print('1:', clone1)
    clone1=clone1.lstrip()
    print('2:', clone1)
    clone1 = ''.join([i for i in clone1 if not i.isdigit()])
    print('3:', clone1)
    #lone1 =''.join(e for e in clone1 if e.isalpha())
    clone1 = remove_accents(clone1)
    print('4:', clone1)
    try:
        #lone1 = re.sub(r'\[\]',r'',clone1)
        #lone1 = clone1("][","")
        #lone1 = clone1.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
        clone1 = clone1[:-2]
        print('5:', clone1)
    except:
        pass
    poc.name=clone1

    # 2) create slug from name (lower case, get rid of special characters, numbers, spaces)
    clone2 = row[1][:]
    print('6:', clone2)
    clone2=clone2.lower()
    print('7:', clone2)
    clone2 =''.join(e for e in clone2 if e.isalpha())
    print('8:', clone2)
    #tring  = unicode(string, "utf-8")
    #tring = unidecode(string)
    clone2 = remove_accents(clone2)
    print('8:', clone2)
    poc.slug = clone2

    # 3) if name is 'Vi Duc Hoi', image.name should be 'Vi_Duc_Hoi.jpg'
    clone3 = row[1][:]
    print('8:', clone3)
    clone3=clone3.lstrip()
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
    poc.image.name = clone3

    # 4) tag is a foreign key
    clone4=row[0][:]
    clone4=clone4.lower()
    clone4 = clone4.replace('_','')
    print('17:', clone4)
    tag=Tag.objects.get(slug=clone4)
    print('18:', tag.name)
    poc.tag=tag
    print('19:', poc.tag)

    # 5) if name is 'Vi Duc Hoi', link should be 'https://en.wikipedia.org/wiki/Vi_Duc_Hoi'
    clone5 = row[1][:]
    print('20:', clone5)
    clone5=clone5.lstrip()
    print('21:', clone5)
    clone5 = clone5.replace(' ','_')
    print('22:', clone5)
    clone5 = ''.join([i for i in clone5 if not i.isdigit()])
    print('24:', clone5)
    try:
        clone5 = clone5.rstrip(']')
        print('25:', clone5)
        clone5 = clone5.rstrip('[')
        print('26:', clone5)
    except:
        pass
    clone5='https://en.wikipedia.org/wiki/'+clone5
    print('27:', clone5)
    clone5 = remove_accents(clone5)
    print('28:', clone5)
    poc.link = clone5
    print('29:', clone5)

  except:
    pass
  poc.save()
