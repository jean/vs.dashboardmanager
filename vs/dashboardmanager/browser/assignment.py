
from zope.component import getUtility, getMultiAdapter
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlets.interfaces import IPortletManager, IPortletAssignment, IPortletAssignmentMapping

class AssignmentView(BrowserView):

    template = ViewPageTemplateFile('assignment.pt')

    def getRoles(self):
        mt = getToolByName(self, 'portal_membership')
        return  sorted([r for r in mt.getPortalRoles() if r != 'Owner'])

    def push_assignment(self, userid='', roles=[]):

        for i in range(1, 5):
            manager_name = 'vs.dashboardmanager.column%d' % i
            print '-'*80
            print manager_name
            manager = getUtility(IPortletManager, name=manager_name, context= self.context)
            mapping = getMultiAdapter((self.context, manager), IPortletAssignmentMapping)
            for id, assignment in mapping.items():
                print id, assignment

        return 'done'


    def __call__(self, *args, **kw):
        return self.template(*args, **kw)


