################################################################
# vs.dashboardmanager
# (C) 2010, Veit Schiele & Andreas Jung
# Published under the GNU Public Licence V 2 (GPL 2)
################################################################

import config
from cStringIO import StringIO
from Products.CMFCore.utils import getToolByName

class Generator(object):

    def installProducts(self, p, out):
        """QuickInstaller install of required Products"""
        qi = getToolByName(p, 'portal_quickinstaller')
        for product in config.DEPENDENCIES:
            if qi.isProductInstalled(product):
                qi.reinstallProducts([product])
            else:
                qi.installProduct(product, locked=0)
                print >> out, "Product installed: %s \n" %product


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    if context.readDataFile('vs.dashboardmanager_various.txt') is None:
        return

    # Add additional setup code here
    out = StringIO()
    site = context.getSite()
    gen = Generator()
    gen.installProducts(site, out)
    logger = context.getLogger(config.PROJECTNAME)
    logger.info(out.getvalue())

