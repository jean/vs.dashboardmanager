from Products.CMFCore.utils import getToolByName

from vs.dashboardmanager.config import PROJECTNAME

def remove_configlet(context):
    controlpanel = getToolByName(context, 'portal_controlpanel', None)
    if controlpanel:
        controlpanel.unregisterConfiglet('vs_dashboard_management')

def uninstall(portal):
    remove_configlet(portal)

