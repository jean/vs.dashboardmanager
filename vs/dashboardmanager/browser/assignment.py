
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AssignmentView(BrowserView):

    template = ViewPageTemplateFile('assignment.pt')

    def getRoles(self):
        mt = getToolByName(self, 'portal_membership')
        return  sorted([r for r in mt.getPortalRoles() if r != 'Owner'])

    def push_assignment(self, userid='', roles=[]):
        return 'done'


    def __call__(self, *args, **kw):
        return self.template(*args, **kw)


