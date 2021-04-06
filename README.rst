Wagtail Editor Extensions
=========================

Text styling additions for Wagtail's DraftJS editor.

Installation
------------

.. code:: bash

   pip install wagtail-editor-extensions

Setup
-----

Add to installed app:

.. code:: python

   INSTALLED_APPS = [
      ...
      'wagtail_editor_extensions',
      ...
   ]

Settings
--------

.. code:: python

   # picker icon
   WAGTAILEDITOREXTENSIONS_ICON = ['...']
   # Add your colours
   WAGTAILEDITOREXTENSIONS_COLOURS = {
      'black': '#000000',
      'white': '#ffffff'
   }
   # Add highlight colours
   WAGTAILEDITOREXTENSIONS_HIGHLIGHT = {
      'black': '#000000',
      'white': '#ffffff'
   }
   # Add font sizes
   WAGTAILEDITOREXTENSIONS_FONT_SIZE = {
      '10': '10',
      '12': '12'
   }
   # Add line spacing
   WAGTAILEDITOREXTENSIONS_LINE_SPACE = {
      '1.0': '1.0',
      '1.15': '1.15'
   }

Screenshots
-----------

.. figure::  http://wagtailcolourpicker.readthedocs.io/en/latest/_images/screen_1.png
   :width: 728 px

Picker

.. figure:: http://wagtailcolourpicker.readthedocs.io/en/latest/_images/screen_2.png
   :width: 728 px

Selected Text

Example site with docker
------------------------

Clone the repo

.. code:: bash

    $ git clone https://github.com/mattdood/wagtail-editor-extensions.git

Run the docker container

.. code:: bash

    $ cd wagtail-editor-extensions
    $ docker-compose up

Create yourself a superuser

.. code:: bash

    $ docker-compose run --rm app python manage.py createsuperuser

Go to http://127.0.0.1:8000/cms and add a new basic page
