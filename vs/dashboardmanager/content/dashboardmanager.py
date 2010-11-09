# -*- coding: utf-8 -*-
"""Definition of the DashboardManager content type
"""
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from collective.portletpage.content import PortletPage, PortletPageSchema
from vs.dashboardmanager import config
from vs.dashboardmanager.interfaces import IDashboardManager
from zope.interface import implements

class DashboardManager(PortletPage):
    """a dashboardmanager"""
    
    implements(IDashboardManager)
    security = ClassSecurityInfo()

    meta_type = "DashboardManager"
    schema = PortletPageSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
atapi.registerType(DashboardManager, config.PROJECTNAME)
