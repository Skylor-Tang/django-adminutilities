=====================
django-adminutilities
=====================


.. image:: https://img.shields.io/pypi/v/django-adminutilities.svg
    :target: https://pypi.python.org/pypi/django-adminutilities

Allow calling registered custom functions (system tools, script functions, etc.) via admin UI or `manage.py` command.

The inspiration for this library comes from `https://github.com/timonweb/django-clearcache`.

Installation
------------

1. Install the package via pip:

    .. code-block:: bash

        pip install django-adminutilities

2. Add `adminutilities` to your `INSTALLED_APPS` setting, make sure it's above `django.contrib.admin` like this:

    .. code-block:: python

        INSTALLED_APPS = [
             ...
             'django.contrib.admin',
             'adminutilities',
        ]

3. Add `adminutilities.middleware.GetAllAdminToolFunctionsMiddleware` to your `MIDDLEWARE` setting like this:

    .. code-block:: python

        MIDDLEWARE = [
             ...
             'adminutilities.middleware.GetAllAdminToolFunctionsMiddleware',
        ]

4. Add `adminutilities` to your `urls.py`:

    .. code-block:: python

        urlpatterns = [
             ...
             path('admin/', admin.site.urls),
             path('admin/adminutilities/', include('adminutilities.urls')),
        ]

Usage
-----

1. Create a new file `admin_tools.py` in your app folder, and define your custom functions, for example:

    .. code-block:: python

        from adminutilities.decorators import admin_tool

        @admin_tool
        def my_custom_function():
             return 'Hello, world!'

2. Go to `/admin/adminutilities/` and you will see the registered functions. If you click the function, it will execute the function and show the result.

3. You can also call the function via `manage.py` command, need to provide the full path of the function (`app_name.function_name`), for example:

    .. code-block:: bash

        python manage.py adminutilities main.my_custom_function

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
