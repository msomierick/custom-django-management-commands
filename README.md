This is the code for the [custom Django management commands](http://erickmbwana.gitlab.io/2017/07/16/custom-django-management-commands/) tutorial

For quick local gratification, do the following:

```
$ git clone https://github.com/msomierick/custom-django-management-commands stockrecords

$ cd stockrecords

# In a virtualenv
$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py populatestocks 1000

$ python manage.py runserver
```

Visit the Django admin in to see changes.

To run the tests:

`$ python manage.py test main `
