import unittest

from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase

from vs.dashboardmanager.config import PROJECTNAME
from vs.dashboardmanager.tests.layer import DashboardManagerLayer

TYPES = (
    'DashboardManager',
    )

STYLESHEETS = (
    '++resource++vs.dashboardmanager.css',
    '++resource++vs.dashboardmanager.autocomplete.css',
    )

JAVASCRIPTS = (
    '++resource++vs.dashboardmanager.autocomplete.js',
    )

CONFIGLETS = (
    'vs_dashboard_management',
    )

class InstallTest(PloneTestCase):
    
    layer = DashboardManagerLayer

    def test_types(self):
        for t in TYPES:
            self.failUnless(t in self.portal.portal_types.objectIds(), '%s content type not installed' % t)

    def test_portal_factory(self):
        for t in TYPES:
            self.failUnless(t in self.portal.portal_factory.getFactoryTypes().keys(), '%s portal factory not installed' % t)

    def test_stylesheets(self):
        for css in STYLESHEETS:
            self.failUnless(css in self.portal.portal_css.getResourceIds(), '%s stylesheet not installed' % css)

    def test_javascripts(self):
        for js in JAVASCRIPTS:
            self.failUnless(js in self.portal.portal_javascripts.getResourceIds(), '%s javascript not installed' % js)

    def test_configlets(self):
        installed = [a.getAction(self)['id'] for a in self.portal.portal_controlpanel.listActions()]
        for c in CONFIGLETS:
            self.failUnless(c in installed, '%s configlet not installed' % c)

    def test_catalog_index_metadata(self):
        self.failUnless('dashboardmanager_groups' in self.portal.portal_catalog.indexes())
        self.failUnless('getUsedForGroups' in self.portal.portal_catalog.schema())

    def test_portlets(self):
        self.fail('To be implemented...')

    def test_viewlets(self):
        self.fail('To be implemented...')

class UninstallTest(PloneTestCase):

    layer = DashboardManagerLayer

    def afterSetUp(self):
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_product_uninstall(self):
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))

    def test_types(self):
        for t in TYPES:
            self.failIf(t in self.portal.portal_types.objectIds(), '%s content type not uninstalled' % t)

    def test_portal_factory(self):
        for t in TYPES:
            self.failIf(t in self.portal.portal_factory.getFactoryTypes().keys(), '%s portal factory not uninstalled' % t)

    def test_stylesheets(self):
        for css in STYLESHEETS:
            self.failIf(css in self.portal.portal_css.getResourceIds(), '%s stylesheet not installed' % css)

    def test_javascripts(self):
        for js in JAVASCRIPTS:
            self.failIf(js in self.portal.portal_javascripts.getResourceIds(), '%s javascript not installed' % js)

    def test_configlets(self):
        installed = [a.getAction(self)['id'] for a in self.portal.portal_controlpanel.listActions()]
        for c in CONFIGLETS:
            self.failIf(c in installed, '%s configlet not uninstalled' % c)

    def test_portlets(self):
        self.fail('To be implemented...')

    def test_viewlets(self):
        self.fail('To be implemented...')

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

