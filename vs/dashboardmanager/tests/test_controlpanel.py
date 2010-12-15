import unittest

from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase

from vs.dashboardmanager.tests.layer import DashboardManagerLayer

class DashboardManagerTest(PloneTestCase):

    layer = DashboardManagerLayer

    def test_controlpanel_view(self):
        # dashboard manager setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST), name='dashboard-manager')
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_view_protected(self):
        # dashboard manager setting control panel view can not be accessed by anonymous users
        from AccessControl import Unauthorized
        self.logout()
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse, '@@dashboard-manager')
        
def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

