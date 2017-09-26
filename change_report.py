from nutr.models import POC
for n in POC.audit_log.values():
  #rint (n)
  #rint ("n is a ",type(n))
  #rint ("let's see what's in that dictionary: ")
  #or k in n:
    #rint (k,":",n[k])
  #rint (n['slug'],' created or updated by ',n['modified_by_id'],n['created'])
  #rint ("%d was created by %d             %s" % (n['id'],n['modified_by_id'],n['created']))
  print ("%d	%s	%s	%s	%s	%d" %  (n['id'], n['action_type'], \
    n['created_by_id'], n['action_date'], n['created_by_id'], n['tag_id']))
  #n['created_by_id'])
