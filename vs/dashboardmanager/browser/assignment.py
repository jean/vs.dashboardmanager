
from zope.component import getUtility, getMultiAdapter
from zope.app.container.interfaces import INameChooser
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlets.interfaces import IPortletManager, IPortletAssignment, IPortletAssignmentMapping
from plone.app.portlets.utils import assignment_mapping_from_key

class AssignmentView(BrowserView):

    template = ViewPageTemplateFile('assignment.pt')

    def getRoles(self):
        mt = getToolByName(self, 'portal_membership')
        return  sorted([r for r in mt.getPortalRoles() if r != 'Owner'])

    def push_assignment(self, userid='', roles=[]):
        """ Push all assignment portlet page assignment into the
            dashboard of a user or a group of users.
        """

        site = getUtility(ISiteRoot)

        # iterate over all configured portlet managers for PortletPage
        for i in range(1, 5):

            manager_name = 'vs.dashboardmanager.column%d' % i
            manager = getUtility(IPortletManager, name=manager_name, context= self.context)
            mapping = getMultiAdapter((self.context, manager), IPortletAssignmentMapping)

            # get hold of the user dashboard manager
            manager2 = getUtility(IPortletManager, name='plone.dashboard%d' % i)
            mapping2 = assignment_mapping_from_key(site, 
                                                  'plone.dashboard%d' % i, 
                                                   category='user', 
                                                   key=userid, 
                                                   create=True)
            # and copy over the assignments
            for id, assignment in mapping.items():
                mapping2[id] = assignment

        return self.request.response.redirect(self.context.absolute_url())


    def __call__(self, *args, **kw):
        return self.template(*args, **kw)


