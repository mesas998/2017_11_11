2017-06-24T19:24:29.938467+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:24:29.938468+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:24:29.938469+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Liu_Xiaobo.jpg'}
2017-06-24T19:24:29.938471+00:00 app[web.1]: 
2017-06-24T19:24:29.938471+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.938472+00:00 app[web.1]: 
2017-06-24T19:24:29.938473+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.938473+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T19:24:29.938475+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:24:29.938475+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:24:29.938476+00:00 app[web.1]: 
2017-06-24T19:24:29.938476+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.938477+00:00 app[web.1]: 
2017-06-24T19:24:29.938477+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.938478+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:24:29.938479+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:24:29.938479+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:24:29.938480+00:00 app[web.1]: 
2017-06-24T19:24:29.938481+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.938481+00:00 app[web.1]: 
2017-06-24T19:24:29.938482+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.938483+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:24:29.938483+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:24:29.938484+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:24:29.938484+00:00 app[web.1]: 
2017-06-24T19:24:29.938485+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.938485+00:00 app[web.1]: 
2017-06-24T19:24:29.938486+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.938487+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:24:29.938489+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>"
2017-06-24T19:24:29.939381+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T19:24:29.938487+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:24:29.939383+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.939384+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T19:24:29.939385+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T19:24:29.939386+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:24:29.939386+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:24:29.939387+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Liu_Xiaobo.jpg'}
2017-06-24T19:24:29.939388+00:00 app[web.1]: 
2017-06-24T19:24:29.939389+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.939390+00:00 app[web.1]: 
2017-06-24T19:24:29.939390+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.939391+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T19:24:29.939392+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:24:29.939393+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:24:29.939393+00:00 app[web.1]: 
2017-06-24T19:24:29.939394+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.939395+00:00 app[web.1]: 
2017-06-24T19:24:29.939395+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.939396+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:24:29.939397+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:24:29.939397+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:24:29.939398+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.939398+00:00 app[web.1]: 
2017-06-24T19:24:29.939399+00:00 app[web.1]: 
2017-06-24T19:24:29.939400+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.939401+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:24:29.939401+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:24:29.939402+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:24:29.939403+00:00 app[web.1]: 
2017-06-24T19:24:29.939403+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.939404+00:00 app[web.1]: 
2017-06-24T19:24:29.939405+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.939405+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:24:29.939406+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:24:29.939410+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>"
2017-06-24T19:24:29.940212+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T19:24:29.940214+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.940215+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T19:24:29.940216+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T19:24:29.940216+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:24:29.940217+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:24:29.940218+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Liu_Xiaobo.jpg'}
2017-06-24T19:24:29.940218+00:00 app[web.1]: 
2017-06-24T19:24:29.940219+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.940220+00:00 app[web.1]: 
2017-06-24T19:24:29.940221+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.940221+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T19:24:29.940222+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:24:29.940223+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:24:29.940230+00:00 app[web.1]: 
2017-06-24T19:24:29.940230+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.940231+00:00 app[web.1]: 
2017-06-24T19:24:29.940232+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.940232+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:24:29.940233+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:24:29.940233+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:24:29.940234+00:00 app[web.1]: 
2017-06-24T19:24:29.940234+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.940235+00:00 app[web.1]: 
2017-06-24T19:24:29.940236+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.940236+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:24:29.940237+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:24:29.940238+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:24:29.940238+00:00 app[web.1]: 
2017-06-24T19:24:29.940239+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:24:29.940239+00:00 app[web.1]: 
2017-06-24T19:24:29.940240+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:24:29.940241+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:24:29.940241+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:24:29.940246+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>"
