2017-06-24T20:12:13.212705+00:00 app[web.1]: 
2017-06-24T20:12:13.212705+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.212706+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T20:12:13.212707+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T20:12:13.212707+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T20:12:13.212708+00:00 app[web.1]: 
2017-06-24T20:12:13.212709+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.212709+00:00 app[web.1]: 
2017-06-24T20:12:13.212710+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.212711+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T20:12:13.212711+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T20:12:13.212785+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>"
2017-06-24T20:12:13.213864+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T20:12:13.213865+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.213866+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T20:12:13.213867+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T20:12:13.213868+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T20:12:13.213869+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T20:12:13.213869+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'favicon.ico'}
2017-06-24T20:12:13.213871+00:00 app[web.1]: 
2017-06-24T20:12:13.213870+00:00 app[web.1]: 
2017-06-24T20:12:13.213872+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.213871+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.213873+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T20:12:13.213873+00:00 app[web.1]:     current = current[bit]
2017-06-24T20:12:13.213874+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T20:12:13.213874+00:00 app[web.1]: 
2017-06-24T20:12:13.213875+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.213876+00:00 app[web.1]: 
2017-06-24T20:12:13.213876+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.213877+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T20:12:13.213878+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T20:12:13.213878+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T20:12:13.213879+00:00 app[web.1]: 
2017-06-24T20:12:13.213879+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.213880+00:00 app[web.1]: 
2017-06-24T20:12:13.213881+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.213881+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T20:12:13.213882+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T20:12:13.213882+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T20:12:13.213883+00:00 app[web.1]: 
2017-06-24T20:12:13.213884+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.213884+00:00 app[web.1]: 
2017-06-24T20:12:13.213885+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.213886+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T20:12:13.213886+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T20:12:13.213887+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>"
2017-06-24T20:12:13.214835+00:00 app[web.1]: Exception while resolving variable 'name' in template 'unknown'.
2017-06-24T20:12:13.214837+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.214838+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 134, in get_response
2017-06-24T20:12:13.214839+00:00 app[web.1]:     resolver_match = resolver.resolve(request.path_info)
2017-06-24T20:12:13.214839+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/urlresolvers.py", line 404, in resolve
2017-06-24T20:12:13.214840+00:00 app[web.1]:     raise Resolver404({'tried': tried, 'path': new_path})
2017-06-24T20:12:13.214841+00:00 app[web.1]: django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLPattern None ^$>], [<RegexURLResolver <module 'nutr.urls.poc' from '/app/nutr/urls/poc.py'> (None:None) ^poc/>], [<RegexURLResolver <module 'nutr.urls.tag' from '/app/nutr/urls/tag.py'> (None:None) ^tag/>], [<RegexURLResolver <module 'nutr.urls.image' from '/app/nutr/urls/image.py'> (None:None) ^static/>], [<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>]], 'path': 'favicon.ico'}
2017-06-24T20:12:13.214842+00:00 app[web.1]: 
2017-06-24T20:12:13.214842+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.214843+00:00 app[web.1]: 
2017-06-24T20:12:13.214843+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.214844+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 883, in _resolve_lookup
2017-06-24T20:12:13.214845+00:00 app[web.1]:     current = current[bit]
2017-06-24T20:12:13.214845+00:00 app[web.1]: TypeError: 'RegexURLResolver' object is not subscriptable
2017-06-24T20:12:13.214846+00:00 app[web.1]: 
2017-06-24T20:12:13.214847+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.214847+00:00 app[web.1]: 
2017-06-24T20:12:13.214848+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.214848+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 891, in _resolve_lookup
2017-06-24T20:12:13.214849+00:00 app[web.1]:     current = getattr(current, bit)
2017-06-24T20:12:13.214851+00:00 app[web.1]: AttributeError: 'RegexURLResolver' object has no attribute 'name'
2017-06-24T20:12:13.214852+00:00 app[web.1]: 
2017-06-24T20:12:13.214853+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.214853+00:00 app[web.1]: 
2017-06-24T20:12:13.214854+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.214855+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 898, in _resolve_lookup
2017-06-24T20:12:13.214855+00:00 app[web.1]:     current = current[int(bit)]
2017-06-24T20:12:13.214856+00:00 app[web.1]: ValueError: invalid literal for int() with base 10: 'name'
2017-06-24T20:12:13.214856+00:00 app[web.1]: 
2017-06-24T20:12:13.214857+00:00 app[web.1]: During handling of the above exception, another exception occurred:
2017-06-24T20:12:13.214857+00:00 app[web.1]: 
2017-06-24T20:12:13.214858+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:13.214859+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/base.py", line 905, in _resolve_lookup
2017-06-24T20:12:13.214859+00:00 app[web.1]:     (bit, current))  # missing attribute
2017-06-24T20:12:13.214892+00:00 app[web.1]: django.template.base.VariableDoesNotExist: Failed lookup for key [name] in "<RegexURLResolver <module 'user.urls' from '/app/user/urls.py'> (user:dj-auth) ^user/>"
2017-06-24T20:12:28.420671+00:00 heroku[router]: at=info method=GET path="/poc/5" host=stark-springs-75372.herokuapp.com request_id=876690a3-b61a-484a-b75f-18b26340fac7 fwd="161.98.8.8" dyno=web.1 connect=2ms service=6ms status=301 bytes=236 protocol=https
2017-06-24T20:12:28.480562+00:00 heroku[router]: at=info method=GET path="/poc/5/" host=stark-springs-75372.herokuapp.com request_id=b1531cc3-6e42-4072-aff7-444e690708bc fwd="161.98.8.8" dyno=web.1 connect=1ms service=12ms status=200 bytes=374 protocol=https
2017-06-24T20:12:28.473801+00:00 app[web.1]: (0.001) SELECT "nutr_poc"."id", "nutr_poc"."slug", "nutr_poc"."name", "nutr_poc"."image" FROM "nutr_poc" WHERE "nutr_poc"."id" = 5; args=(5,)
2017-06-24T20:12:28.545547+00:00 app[web.1]: Internal Server Error: /static/Leyla_Yunus.jpg
2017-06-24T20:12:28.545550+00:00 app[web.1]: Traceback (most recent call last):
2017-06-24T20:12:28.545551+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 149, in get_response
2017-06-24T20:12:28.545552+00:00 app[web.1]:     response = self.process_exception_by_middleware(e, request)
2017-06-24T20:12:28.545553+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/handlers/base.py", line 147, in get_response
2017-06-24T20:12:28.545554+00:00 app[web.1]:     response = wrapped_callback(request, *callback_args, **callback_kwargs)
2017-06-24T20:12:28.545554+00:00 app[web.1]:   File "/app/nutr/views.py", line 89, in image
2017-06-24T20:12:28.545555+00:00 app[web.1]:     {})
2017-06-24T20:12:28.545556+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/shortcuts.py", line 67, in render
2017-06-24T20:12:28.545557+00:00 app[web.1]:     template_name, context, request=request, using=using)
2017-06-24T20:12:28.545558+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/loader.py", line 96, in render_to_string
2017-06-24T20:12:28.545558+00:00 app[web.1]:     template = get_template(template_name, using=using)
2017-06-24T20:12:28.545559+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/template/loader.py", line 43, in get_template
2017-06-24T20:12:28.545559+00:00 app[web.1]:     raise TemplateDoesNotExist(template_name, chain=chain)
2017-06-24T20:12:28.545651+00:00 app[web.1]: django.template.exceptions.TemplateDoesNotExist: Leyla_Yunus
2017-06-24T20:12:28.723732+00:00 heroku[router]: at=info method=GET path="/static/Leyla_Yunus.jpg" host=stark-springs-75372.herokuapp.com request_id=687ca3e7-747f-44fd-8cbb-58501fe4f8f1 fwd="161.98.8.8" dyno=web.1 connect=1ms service=184ms status=500 bytes=74455 protocol=https
