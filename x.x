2017-06-24T16:08:35.881187+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T16:08:35.881187+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T16:08:35.881189+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Ebrahim_Sharif.jpg'}
2017-06-24T16:08:35.881191+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881190+00:00 app[web.1]: 
2017-06-24T16:08:35.881191+00:00 app[web.1]: 
2017-06-24T16:08:35.881192+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881193+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T16:08:35.881194+00:00 app[web.1]:     current = current[bit]
2017-06-24T16:08:35.881194+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T16:08:35.881195+00:00 app[web.1]: 
2017-06-24T16:08:35.881207+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881208+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881208+00:00 app[web.1]: 
2017-06-24T16:08:35.881209+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T16:08:35.881210+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T16:08:35.881211+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T16:08:35.881211+00:00 app[web.1]: 
2017-06-24T16:08:35.881212+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881212+00:00 app[web.1]: 
2017-06-24T16:08:35.881213+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881214+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T16:08:35.881214+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T16:08:35.881215+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T16:08:35.881216+00:00 app[web.1]: 
2017-06-24T16:08:35.881216+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881217+00:00 app[web.1]: 
2017-06-24T16:08:35.881217+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881218+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T16:08:35.881219+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T16:08:35.881224+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>"
2017-06-24T16:08:35.881962+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T16:08:35.881964+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T16:08:35.881963+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881965+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T16:08:35.881966+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T16:08:35.881966+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T16:08:35.881968+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Ebrahim_Sharif.jpg'}
2017-06-24T16:08:35.881968+00:00 app[web.1]: 
2017-06-24T16:08:35.881969+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881970+00:00 app[web.1]: 
2017-06-24T16:08:35.881970+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881971+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T16:08:35.881972+00:00 app[web.1]:     current = current[bit]
2017-06-24T16:08:35.881972+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T16:08:35.881973+00:00 app[web.1]: 
2017-06-24T16:08:35.881974+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881974+00:00 app[web.1]: 
2017-06-24T16:08:35.881975+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881976+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T16:08:35.881976+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T16:08:35.881977+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T16:08:35.881978+00:00 app[web.1]: 
2017-06-24T16:08:35.881978+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881979+00:00 app[web.1]: 
2017-06-24T16:08:35.881979+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881981+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T16:08:35.881980+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T16:08:35.881981+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T16:08:35.881982+00:00 app[web.1]: 
2017-06-24T16:08:35.881983+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.881984+00:00 app[web.1]: 
2017-06-24T16:08:35.881984+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.881985+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T16:08:35.881986+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T16:08:35.881989+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>"
2017-06-24T16:08:35.883158+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T16:08:35.883159+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.883160+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T16:08:35.883160+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T16:08:35.883161+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T16:08:35.883162+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T16:08:35.883163+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/Ebrahim_Sharif.jpg'}
2017-06-24T16:08:35.883164+00:00 app[web.1]: 
2017-06-24T16:08:35.883165+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.883165+00:00 app[web.1]: 
2017-06-24T16:08:35.883166+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.883167+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T16:08:35.883167+00:00 app[web.1]:     current = current[bit]
2017-06-24T16:08:35.883168+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T16:08:35.883169+00:00 app[web.1]: 
2017-06-24T16:08:35.883169+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.883170+00:00 app[web.1]: 
2017-06-24T16:08:35.883170+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.883171+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T16:08:35.883172+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T16:08:35.883173+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T16:08:35.883173+00:00 app[web.1]: 
2017-06-24T16:08:35.883174+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.883174+00:00 app[web.1]: 
2017-06-24T16:08:35.883175+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.883176+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T16:08:35.883176+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T16:08:35.883177+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T16:08:35.883177+00:00 app[web.1]: 
2017-06-24T16:08:35.883178+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T16:08:35.883179+00:00 app[web.1]: 
2017-06-24T16:08:35.883179+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T16:08:35.883180+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T16:08:35.883180+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T16:08:35.883184+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>"
