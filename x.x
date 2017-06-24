2017-06-24T19:59:04.964514+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:59:04.964506+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T19:59:04.964507+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:59:04.964507+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:59:04.964514+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:59:04.964509+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern nutr_image ^(?P<jpg>[\w\-]+).jpg$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^static\/(?P<path>.*)$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^app\/epa7658577\/images\/(?P<path>.*)$>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/site/style.css'}
2017-06-24T19:59:04.964516+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.964515+00:00 app[web.1]: 
2017-06-24T19:59:04.964516+00:00 app[web.1]: 
2017-06-24T19:59:04.964517+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.964518+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:59:04.964518+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:59:04.964519+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:59:04.964519+00:00 app[web.1]: 
2017-06-24T19:59:04.964520+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.964521+00:00 app[web.1]: 
2017-06-24T19:59:04.964521+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.964522+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:59:04.964523+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:59:04.964524+00:00 app[web.1]: 
2017-06-24T19:59:04.964523+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:59:04.964524+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.964525+00:00 app[web.1]: 
2017-06-24T19:59:04.964526+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.964526+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:59:04.964527+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:59:04.964532+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>"
2017-06-24T19:59:04.965410+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T19:59:04.965411+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965412+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T19:59:04.965413+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T19:59:04.903561+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965426+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:59:04.965427+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:59:04.965431+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern nutr_image ^(?P<jpg>[\w\-]+).jpg$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^static\/(?P<path>.*)$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^app\/epa7658577\/images\/(?P<path>.*)$>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/site/style.css'}
2017-06-24T19:59:04.965432+00:00 app[web.1]: 
2017-06-24T19:59:04.965433+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.965434+00:00 app[web.1]: 
2017-06-24T19:59:04.965434+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965435+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T19:59:04.965436+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:59:04.965437+00:00 app[web.1]: 
2017-06-24T19:59:04.965438+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.965438+00:00 app[web.1]: 
2017-06-24T19:59:04.965440+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:59:04.965439+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965441+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:59:04.965439+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:59:04.965441+00:00 app[web.1]: 
2017-06-24T19:59:04.965436+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:59:04.965442+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.965443+00:00 app[web.1]: 
2017-06-24T19:59:04.965443+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965444+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:59:04.965444+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:59:04.965445+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:59:04.965454+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.965446+00:00 app[web.1]: 
2017-06-24T19:59:04.965455+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:59:04.965456+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:59:04.965454+00:00 app[web.1]: 
2017-06-24T19:59:04.965455+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.965460+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>"
2017-06-24T19:59:04.966925+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T19:59:04.966927+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.966928+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T19:59:04.966929+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T19:59:04.966931+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T19:59:04.966932+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T19:59:04.966933+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern nutr_image ^(?P<jpg>[\w\-]+).jpg$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^static\/(?P<path>.*)$>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>, <RegexURLPattern None ^app\/epa7658577\/images\/(?P<path>.*)$>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'static/site/style.css'}
2017-06-24T19:59:04.966935+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.966935+00:00 app[web.1]: 
2017-06-24T19:59:04.966936+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.966936+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T19:59:04.966937+00:00 app[web.1]:     current = current[bit]
2017-06-24T19:59:04.966934+00:00 app[web.1]: 
2017-06-24T19:59:04.966938+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T19:59:04.966938+00:00 app[web.1]: 
2017-06-24T19:59:04.966939+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.966939+00:00 app[web.1]: 
2017-06-24T19:59:04.966940+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.966941+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T19:59:04.966942+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T19:59:04.966942+00:00 app[web.1]: 
2017-06-24T19:59:04.966940+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T19:59:04.966943+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.966943+00:00 app[web.1]: 
2017-06-24T19:59:04.966944+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.966945+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T19:59:04.966945+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T19:59:04.966946+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T19:59:04.966947+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T19:59:04.966948+00:00 app[web.1]: 
2017-06-24T19:59:04.966948+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T19:59:04.966947+00:00 app[web.1]: 
2017-06-24T19:59:04.966949+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T19:59:04.966950+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T19:59:04.966981+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>"
2017-06-24T19:59:31.778061+00:00 heroku[router]: at=info method=GET path="/static/Leyla_Yunus.jpg" host=fathomless-wildwood-30026.herokuapp.com request_id=3f32f8cf-b005-4222-bb05-3d2b9865b5f1 fwd="161.98.8.8" dyno=web.1 connect=0ms service=2ms status=200 bytes=218 protocol=https
2017-06-24T19:59:31.704679+00:00 app[web.1]: (0.001) SELECT "nutr_poc"."id", "nutr_poc"."slug", "nutr_poc"."name", "nutr_poc"."image" FROM "nutr_poc" WHERE "nutr_poc"."id" = 5; args=(5,)
2017-06-24T19:59:31.719088+00:00 heroku[router]: at=info method=GET path="/poc/5/" host=fathomless-wildwood-30026.herokuapp.com request_id=ba947131-9f97-4e7e-ad2d-5be041081c39 fwd="161.98.8.8" dyno=web.1 connect=0ms service=18ms status=200 bytes=374 protocol=https
