from nutr.models import POC
for n in POC.audit_log.values():
  print ("%d	%s	%s	%s	%s	%d" %  (n['id'], n['action_type'], \
    n['created_by_id'], n['action_date'], n['created_by_id'], n['tag_id']))

"""
  print (n)
  print ("n is a ",type(n))
  print ("let's see what's in that dictionary: ")
  for k in n:
    print (k,":",n[k])
  print (n['slug'],' created or updated by ',n['modified_by_id'],n['created'])
  print ("%d was created by %d             %s" % (n['id'],n['modified_by_id'],n['created']))
"""
