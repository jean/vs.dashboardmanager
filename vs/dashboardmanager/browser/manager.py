import time
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ManagementView(BrowserView):

    template = ViewPageTemplateFile('management.pt')
    template_folder_id = 'dashboard-templates'

    def foo(self):
        return 'bar'

    def available_dashboard_pages(self):
        """ return list of available dashboard templates """

        catalog = getToolByName(self, 'portal_catalog')
        return catalog(portal_type='Portlet Page', sort_on='getObjPositionInParent')

    def new_dashboard_page(self):
        """ Create a new dashboard page inside the dedicated 
            dashboard templates folder.
        """

        portal_root = self.context.restrictedTraverse('@@plone').context
        if not self.template_folder_id in portal_root.objectIds():
            portal_root.invokeFactory('Folder', id=self.template_folder_id)
            folder = portal_root[self.template_folder_id]
            folder.setTitle(u'Templates for dashboard portlet pages')
            folder.reindexObject()
        else:
            folder = portal_root[self.template_folder_id]

        self.request.response.redirect(folder.absolute_url() + '/portal_factory/Portlet Page/%s/edit' % time.time())




    def __call__(self, *args, **kw):
        return self.template(*args, **kw)
