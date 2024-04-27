1.Start Django-project and app

```
    $ django-admin startprojects ...
    $ django-admin startapp ...
```

2.Add the following lines to the settings.py of your file

```
    INSTALLED_APPS = [
         ...
        'food',
         ...
    ]
    TEMPLATES = [
        {
            ...
            "DIRS": [BASE_DIR / 'templates'],
            ...
        },
    ]
```
3.When you create, modify, or delete models, you need to create a new migration.

```
    $ python manage.py makemigrations
```

4.Once you have created the migration files, the next step is to apply these migrations to the database to ensure that the database structure remains synchronized with your models.

```
    $ python manage.py migrate
```