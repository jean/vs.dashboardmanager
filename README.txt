vs.dashboardmanager
===================

``vs.dashboardmanager`` provides a templating mechanism for dashboard pages and
a push mechanism for transfering portlets of dashboard template pages into the
dashboard of individual site members or all members of a Plone group. Consider 
``vs.dashboardmanager`` as a kind of remote adminstration tool for dashboards.


Installation
============

* add ``vs.dashboardmanager`` to the ``eggs`` and ``zcml`` options of 
  your buildout.cfg and re-run buildout (under Plone 4 you can omit the
  ``zcml`` slug)

* either create a new Plone site using the ``Dashboard Manager`` extension profile
  or install it through the Plone site setup control panel

Usage
=====

* use the dashboard management option from the Plone control panel or add
  ``@@dashboard-manager`` to the URL of the Plone site

* create a new Dashboard Manager (standard content-type and available as add-able 
  content from the standard "Add" drop-down in the folder contents view 
  with some portlets (using the ``Portlets`` tab) 

* push the portlet into the dashboard of a user or a group using 
  the ``assigments`` tab of the Dashboard Manager


Tested
======
* tested with Plone 3.3.X
* tested with Plone 4.0.X

Licence
=======
``vs.dashboardmanager`` is published under the GNU Public Licence V 2 (GPL 2)

Credits
=======
``vs.dashboardmanager`` is based and influenced by ``collective.portletpage``
by Martin Aspeli. ``vs.dashboardmanager`` is uses in parts of
``collective.portletpage``.

Thanks to Veit Schiele and Immanuel Diakonie Group for the funding.

Carsten Raddatz provided the german translation.

Authors
=======

| Andreas Jung 
| info@zopyx.com
| www.zope.com
|
| Veit Schiele
| kontakt@veit-schiele.de
| www.veit-schiele.de


