from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import ptc
from Products.PloneTestCase import layer
from Products.Five import zcml
from Products.Five import fiveconfigure

ptc.setupPloneSite(
    extension_profiles=('vs.dashboardmanager:default', )
)

class DashboardManagerLayer(layer.PloneSite):
    """Configure vs.dashboardmanager"""

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import vs.dashboardmanager
        zcml.load_config("configure.zcml", vs.dashboardmanager)
        fiveconfigure.debug_mode = False
        ztc.installPackage("vs.dashboardmanager", quiet=1)

    @classmethod
    def tearDown(cls):
        pass

