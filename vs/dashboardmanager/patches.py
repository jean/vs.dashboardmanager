
from plone.portlets.interfaces import IPortletType
from zope.component import adapts, getMultiAdapter, getUtilitiesFor

"""
Monkey-patching PortletManager as workaround for 
http://lists.plone.org/pipermail/product-developers/2010-July/005115.html
"""

def getAddablePortletTypes(self):
    
    addable = []
    for p in getUtilitiesFor(IPortletType):
        #BBB - first condition, because starting with Plone 3.1
        #every p[1].for_ should be a list
        if not isinstance(p[1].for_, list):
            logger.warning("Deprecation Warning Portlet type " + \
              "%s is using a deprecated format for " % p[1].addview + \
              "storing interfaces of portlet managers where it is " + \
              "addable. Its for_ attribute should be a list of portlet " + \
              "manager interfaces, using [zope.interface.Interface] " + \
              "for the portlet type to be addable anywhere. The old " + \
              "format will be unsupported in Plone 4.0.")
            if p[1].for_ is None or p[1].for_.providedBy(self):
                addable.append(p[1])
        else:
#            if [i for i in p[1].for_ if i.providedBy(self)]:
            addable.append(p[1])
    return addable

from plone.portlets.manager import PortletManager
PortletManager.getAddablePortletTypes = getAddablePortletTypes

