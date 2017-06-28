(0.001) 
            SELECT name, type FROM sqlite_master
            WHERE type in ('table', 'view') AND NOT name='sqlite_sequence'
            ORDER BY name; args=None
(0.000) SELECT "django_migrations"."app", "django_migrations"."name" FROM "django_migrations"; args=()
(0.000) PRAGMA foreign_keys; args=None
(0.000) PRAGMA foreign_keys = 0; args=None
(0.000) BEGIN; args=None
CREATE TABLE "nutr_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(31) NOT NULL UNIQUE, "slug" varchar(31) NOT NULL UNIQUE); (params None)
(0.000) CREATE TABLE "nutr_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(31) NOT NULL UNIQUE, "slug" varchar(31) NOT NULL UNIQUE); args=None
(0.000) PRAGMA foreign_keys = 0; args=None
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/utils.py", line 62, in execute
    return self.cursor.execute(sql)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/sqlite3/base.py", line 321, in execute
    return Database.Cursor.execute(self, query)
sqlite3.OperationalError: table "nutr_tag" already exists

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "./manage.py", line 22, in <module>
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.4/site-packages/django/core/management/__init__.py", line 353, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.4/site-packages/django/core/management/__init__.py", line 345, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.4/site-packages/django/core/management/base.py", line 348, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/local/lib/python3.4/site-packages/django/core/management/base.py", line 399, in execute
    output = self.handle(*args, **options)
  File "/usr/local/lib/python3.4/site-packages/django/core/management/commands/migrate.py", line 200, in handle
    executor.migrate(targets, plan, fake=fake, fake_initial=fake_initial)
  File "/usr/local/lib/python3.4/site-packages/django/db/migrations/executor.py", line 92, in migrate
    self._migrate_all_forwards(plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/usr/local/lib/python3.4/site-packages/django/db/migrations/executor.py", line 121, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/usr/local/lib/python3.4/site-packages/django/db/migrations/executor.py", line 198, in apply_migration
    state = migration.apply(state, schema_editor)
  File "/usr/local/lib/python3.4/site-packages/django/db/migrations/migration.py", line 123, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/usr/local/lib/python3.4/site-packages/django/db/migrations/operations/models.py", line 59, in database_forwards
    schema_editor.create_model(model)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/base/schema.py", line 284, in create_model
    self.execute(sql, params or None)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/base/schema.py", line 110, in execute
    cursor.execute(sql, params)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/usr/local/lib/python3.4/site-packages/django/db/utils.py", line 95, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/usr/local/lib/python3.4/site-packages/django/utils/six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/utils.py", line 62, in execute
    return self.cursor.execute(sql)
  File "/usr/local/lib/python3.4/site-packages/django/db/backends/sqlite3/base.py", line 321, in execute
    return Database.Cursor.execute(self, query)
django.db.utils.OperationalError: table "nutr_tag" already exists
