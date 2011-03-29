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
  ``@@dashboard-manager`` to the URL of the Plone site to see the dashboard
  manager. It will list the available dashboards. When installed from scratch it
  should say "No portletpage template available".

* create a new Dashboard Manager from the standard "Add" drop-down menu in the
  folder contents view. It is a standard content-type and available anywhere on
  the site.

* provide title, description and body text. This will be shown above the
  portlets the dashboard manager will contain later. Save.

* add some portlets (using the ``Portlets`` tab). The portlets are left as-is
  and may be configured to your liking. You may add up to four portlets here.

* push the portlet into the dashboard of a user or a group using
  the ``assigments`` tab of the Dashboard Manager. Pick a Plone group from the
  drop-down field or type the name of an individual user and push "Assign
  portlets to dashboard(s)".

* as a user that had a dashboard manager assigned to visit the /dashboard. It
  should show the portlets you assigned.

* a portlet page is a page containing portlets as its content and can not be
  assigned to users or roles, but behaves like a normal page. Add portlets using
  the ``Portlets`` tab. The portlets are left as-is and may be configured to your
  liking. You may add up to four portlets here.

* if the is not what you expect check the criteria by which your portlets
  show their content. I.e., the events portlet may show published events only,
  etc.


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
