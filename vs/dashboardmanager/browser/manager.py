################################################################
# vs.dashboardmanager
# (C) 2010, Veit Schiele & Andreas Jung
# Published under the GNU Public Licence V 2 (GPL 2)
################################################################


import time

from AccessControl import getSecurityManager

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from vs.dashboardmanager import MF as _

class ManagementView(BrowserView):

    template = ViewPageTemplateFile('management.pt')
    template_folder_id = 'dashboard-templates'

    def available_dashboard_pages(self):
        """ return list of available dashboard templates """

        catalog = getToolByName(self, 'portal_catalog')
        return catalog(portal_type='DashboardManager', 
                       sort_on='getObjPositionInParent')

    def new_dashboard_page(self):
        """ Create a new dashboard page inside the dedicated 
            dashboard templates folder.
        """

        portal_root = self.context.restrictedTraverse('@@plone').context
        if not self.template_folder_id in portal_root.objectIds():
            portal_root.invokeFactory('Folder', id=self.template_folder_id)
            folder = portal_root[self.template_folder_id]
            folder.setTitle(_(u'Dashboard templates'))
            folder.reindexObject()
        else:
            folder = portal_root[self.template_folder_id]

        self.request.response.redirect(folder.absolute_url() + '/createObject?type_name=Portlet+Page')


    def __call__(self, *args, **kw):
        return self.template(*args, **kw)


class PersonalDashboardView(BrowserView):

    template = ViewPageTemplateFile('my-dashboard-pages.pt')

    def my_dashboard_pages(self):

        user = getSecurityManager().getUser()
        roles = set(user.getRoles())
        catalog = getToolByName(self, 'portal_catalog')

        result = list()
        for brain in catalog(portal_type='DashboardManager'):
            page_roles = set(brain.getUsedForGroups)
            if groups.intersection(page_groups):
                result.append(brain)

        return result

    def __call__(self, *args, **kw):
        return self.template(*args, **kw)
