import unittest

from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase

from vs.dashboardmanager.tests.layer import DashboardManagerLayer

class UninstallTest(PloneTestCase):

    layer = DashboardManagerLayer

    def uninstall(self):
        setup = getToolByName(self.portal, 'portal_setup')
        setup.runAllImportStepsFromProfile('profile-vs.dashboardmanager:uninstall')

    def test_configlet_uninstall(self):
        self.uninstall()
        controlpanel = getattr(self.portal, 'portal_controlpanel')
        installed = [a.getAction(self)['id'] for a in controlpanel.listActions()]
        self.failIf('vs_dashboard_management' in installed)

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

