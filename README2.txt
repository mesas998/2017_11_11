from nutr.models import *
from blog.models import *
Post.objects.count()
post=Post.objects.get(pk=3)
post.title
post.pocs


!!!
WIPES OUT POSTRES ON HEROKU:
$ heroku pg:reset --confirm immense-temple-86427
!!!
pushes local postgres to heroku:
$ heroku pg:push mydb2 DATABASE_URL --app immense-temple-86427
***
https://devcenter.heroku.com/articles/heroku-postgresql
***
$ heroku pg:info
=== DATABASE_URL
Plan:        Hobby-dev
Status:      Available
Connections: 0/20
PG Version:  9.6.2
Created:     2017-07-10 17:59 UTC
Data Size:   7.2 MB
Tables:      0
Rows:        0/10000 (In compliance) <- this should say about 600 rows
Fork/Follow: Unsupported
Rollback:    Unsupported
Add-on:      postgresql-octagonal-93899

$ heroku pg:psql
--> Connecting to postgresql-octagonal-93899
psql (9.6.3, server 9.6.2)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

***
7/10/17 https://devcenter.heroku.com/articles/heroku-postgresql#pg-push-and-pg-pull:
$ heroku addons | grep -i POSTGRES

$ heroku config -s | grep HEROKU_POSTGRESQL
$ heroku addons:create heroku-postgresql:hobby-dev --as POC
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-pointy-53162 as POC_URL
Use heroku addons:docs heroku-postgresql to view documentation

$ heroku config -s | grep POC
POC_URL='postgres://gxtgsrogxtlyyc:6668a0a2ce596011d9b5cf59558ba46c98dad02832b02dcd915a6a65dbbb46d3@ec2-54-235-123-159.compute-1.amazonaws.com:5432/dae0pms3flvn00'
$ heroku help
$ heroku apps
=== michael_sweeney4@yahoo.com Apps
immense-temple-86427

this seems to push postgres tables etc. to heroku:
$ heroku pg:push mydb2 DATABASE_URL --app immense-temple-86427
(https://devcenter.heroku.com/articles/heroku-postgresql#pg-push-and-pg-pull says
This command will take the local database “mylocaldb” and push it to the database at DATABASE_URL on the app “immense-temple-86427”.)

pg_dump: last built-in OID is 16383
pg_dump: reading extensions

$ heroku ps:restart
Restarting dynos on ⬢ serene-caverns-68358... done
$ heroku config
=== stark-peak-45970 Config Vars
DATABASE_URL: postgres://erzvxfqvfotgwa:24616d55faa817c0fadbc620bd6f2f1ebb75f740225524d440819181ea8e3d73@ec2-107-21-113-16.compute-1.amazonaws.com:5432/d2rn7dc8ou73il



***
6/28/17: https://radiant-meadow-96775.herokuapp.com/ | https://git.heroku.com/radiant-meadow-96775.git

6/24/17 13:24: https://young-anchorage-50011.herokuapp.com/
6/24/17 13:57 https://fathomless-wildwood-30026.herokuapp.com/
6/24/17 14:23 https://murmuring-escarpment-53631.herokuapp.com/poc
1a) change DATABASE in settings.py from
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb2',
        'USER': 'michaelsweeney',
        'PASSWORD': 'xzdzxzf',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
} # works on localhost
...to...
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))} # works on heroku
***
1b)
$ for app in $(heroku apps); do heroku apps:destroy --app $app --confirm $app; done
 ▸    Couldn't find that app.
 ▸    Couldn't find that app.
 ▸    Couldn't find that app.
Destroying ⬢ epa7658577 (including all add-ons)... done
Destroying ⬢ shrouded-refuge-87481 (including all add-ons)... done
Michaels-MacBook-Air:epa7658577 michaelsweeney$ heroku create june-12-2017-1045
Creating ⬢ june-12-2017-1045... done
https://june-12-2017-1045.herokuapp.com/ | https://git.heroku.com/june-12-2017-1045.git

2)
$ git init
Reinitialized existing Git repository in /Users/michaelsweeney/epa7658577/.git/
(necessary?)
3) 
$ git add -A

4) (fix quotes)
$ git commit -m "july-5/2017-1300"
[master 095d2b7] june-12/2017-1110
 4 files changed, 68 insertions(+), 28 deletions(-)

(this looks encouraging as I have changed 1 template and 3 nutr/urls files)


5)
$ heroku create
Creating app... done, ⬢ serene-caverns-68358
https://serene-caverns-68358.herokuapp.com/ | https://git.heroku.com/serene-caverns-68358.git
6)
$ git remote -v
heroku	https://git.heroku.com/june-12-2017-1045.git (fetch)
heroku	https://git.heroku.com/june-12-2017-1045.git (push)
origin	https://github.com/mesas998/epa7658577.git (fetch)
origin	https://github.com/mesas998/epa7658577.git (push)


7)
$ git push heroku master
Counting objects: 7651, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6640/6640), done.
Writing objects: 100% (7651/7651), 32.17 MiB | 686.00 KiB/s, done.
Total 7651 (delta 2197), reused 128 (delta 50)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-2.7.13
remote: -----> Installing pip
remote: -----> Installing requirements with pip
remote:        Collecting dj-database-url==0.4.1 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 1))
remote:          Downloading dj-database-url-0.4.1.tar.gz
remote:        Collecting Django==1.9.7 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 2))
remote:          Downloading Django-1.9.7-py2.py3-none-any.whl (6.6MB)
remote:        Collecting gunicorn==19.6.0 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 3))
remote:          Downloading gunicorn-19.6.0-py2.py3-none-any.whl (114kB)
remote:        Collecting psycopg2==2.6.2 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 4))
remote:          Downloading psycopg2-2.6.2.tar.gz (376kB)
remote:        Collecting whitenoise==2.0.6 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 5))
remote:          Downloading whitenoise-2.0.6-py2.py3-none-any.whl
remote:        Collecting requests==2.9.1 (from -r /tmp/build_217d09381952d54a5cbe728095c2f37e/requirements.txt (line 6))
remote:          Downloading requests-2.9.1-py2.py3-none-any.whl (501kB)
remote:        Installing collected packages: dj-database-url, Django, gunicorn, psycopg2, whitenoise, requests
remote:          Running setup.py install for dj-database-url: started
remote:            Running setup.py install for dj-database-url: finished with status 'done'
remote:          Running setup.py install for psycopg2: started
remote:            Running setup.py install for psycopg2: finished with status 'done'
remote:        Successfully installed Django-1.9.7 dj-database-url-0.4.1 gunicorn-19.6.0 psycopg2-2.6.2 requests-2.9.1 whitenoise-2.0.6
remote: 
remote: -----> $ python manage.py collectstatic --noinput
remote:        56 static files copied to '/tmp/build_217d09381952d54a5cbe728095c2f37e/epa7658577/static'.
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 79.9M
remote: -----> Launching...
remote:        Released v4
remote:        https://quiet-woodland-19261.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/serene-caverns-68358.git
 * [new branch]      master -> master


8)
$ heroku open
(opens browser tab with https://quiet-woodland-19261.herokuapp.com/)
(tack /nutrdef or /nutdata or /epacolo onto  URL and voilà!)

9) if epacolo error in browser:
$ heroku logs
requests in requirements.txt not installed?
problem with base template ?



10) 
$ fd
$ pip3.4 install -r requirements.txt

11)
too many rows
get EPAColo down to 1,000 rows or so:
$ ./manage.py shell
from nutr.models import NutData, NutrDef, DataSrc, Datsrcln, EPAColo
>>> EPAColo.objects.get(long=39.827225)
>>> EPAColo.objects.filter(desc__contains='air').delete()


12) rename to old name for Tom and Geoff:
$ heroku apps:rename immense-temple-86427 --app tranquil-waters-57218
Renaming lester-young-86427 to immense-temple-86427... done
https://immense-temple-86427.herokuapp.com/ | https://git.heroku.com/immense-temple-86427.git
Git remote heroku updated
 ▸    Don't forget to update git remotes for all other local checkouts of the app.

13) photos are showing up. 6/24/17 try copying ~/epa7658577/static to ~ and pushing that to heroku (?)
copy image adress from heroku: https://immense-temple-86427.herokuapp.com/static/Liu_Xiaobo.jpg

14) trying to switch to postgres:
http://www.marinamele.com/2014/05/postgresql-on-heroku-and-the-pgbackup-add-on.html
$ heroku addons:add heroku-postgresql:dev
$ heroku config | grep HEROKU_POSTGRESQL
$ heroku addons
Add-on                                            Plan       Price  State  
────────────────────────────────────────────────  ─────────  ─────  ───────
heroku-postgresql (postgresql-aerodynamic-45251)  hobby-dev  free   created
 └─ as DATABASE

The table above shows add-ons and the attachments to the current app (immense-temple-86427) or other apps.
$ heroku pg:info
=== DATABASE_URL
Plan:        Hobby-dev
Status:      Available
Connections: 0/20
PG Version:  9.6.1
Created:     2017-07-03 21:48 UTC
Data Size:   7.2 MB
Tables:      0
Rows:        0/10000 (In compliance)
Fork/Follow: Unsupported
Rollback:    Unsupported
	Add-on:      postgresql-aerodynamic-45251

$ heroku addons:add heroku-postgresql:hobby-basic

Creating heroku-postgresql:hobby-basic on ⬢ immense-temple-86427... !
 ▸    Please verify your account to install this add-on plan (please enter a credit card) For more information, see
 ▸    https://devcenter.heroku.com/categories/billing Verify now at https://heroku.com/verify

heroku maintenance:on
Enabling maintenance mode for ⬢ immense-temple-86427... done

***
:1


