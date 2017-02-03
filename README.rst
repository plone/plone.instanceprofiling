=======================
plone.instanceprofiling
=======================

Profile Plone requests.


How to run for Zope 4, ZServer
==============================

1) Initialize buildout: ``./bootstrap.sh``.

2) Run buildout for Zope 4: ``./bin/buildout -c buildout-zope4.cfg``.

3) Start Zope: ``./bin/instance fg``.

4) Import the ``plone.instanceprofiling:default`` profile to create the contents.

5) Visit ``http://localhost:8080/Plone`` to initialize all Zope caches.

6) Run ``./bin/instanceprofiling`` to start profiling.


How to run for Zope 4, uwsgi
-----------------------------

1) Initialize buildout: ``./bootstrap.sh``.

2) Run buildout for Zope 4: ``./bin/buildout -c buildout-zope4.cfg``.

3) Install uwsgi and requests via: ``./bin/pip install -r requirements.txt``.

4) Start Zope via uwsgi: ``./bin/uwsgi --ini etc/uwsgi.ini``.

4) Import the ``plone.instanceprofiling:default`` profile to create the contents.

5) Visit ``http://localhost:8080/Plone`` to initialize all Zope caches.

6) Run ``./bin/python src/plone/instanceprofiling/profilerunner.py`` to start profiling.


How to run for Zope 2, ZServer
==============================

1) Initialize buildout: ``./bootstrap.sh``.

2) Run buildout for Zope 4: ``./bin/buildout -c buildout-zope2.cfg``.

3) Start Zope: ``./bin/instance fg``.

4) Import the ``plone.instanceprofiling:default`` profile to create the contents.

5) Visit ``http://localhost:8080/Plone`` to initialize all Zope caches.

6) Run ``./bin/instanceprofiling`` to start profiling.


Example test run results
========================


Test run with Plone 5.1 on Zope 4 and ZServer
---------------------------------------------

Minimum request time: 0.190841913223
Maximum request time: 0.404036045074
Average request time: 0.250301946131
Median request time: 0.247586965561
Total running time: 100.371080399


Test run with Plone 5.1 on Zope 4 and uwsgi
-------------------------------------------

Minimum request time: 0.144521951675
Maximum request time: 0.380453824997
Average request time: 0.226307987275
Median request time: 0.226958990097
Total running time: 90.7495028973


Test run with Plone 5.1 on Zope 2 and ZServer
---------------------------------------------

Minimum request time: 0.587725162506
Maximum request time: 0.817272901535
Average request time: 0.672410908483
Median request time: 0.649533033371
Total running time: 269.636774302


License
-------

The project is licensed under the GPLv2.
