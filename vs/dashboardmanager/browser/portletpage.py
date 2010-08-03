################################################################
# vs.dashboardmanager
# (C) 2010, Veit Schiele & Andreas Jung
# Published under the GNU Public Licence V 2 (GPL 2)
################################################################


from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import ManagePortal
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Base(BrowserView):
    """Base class for index page views
    """

class PortletPageView(Base):
    """Default view for PortletPage """

    def isManager(self):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getAuthenticatedMember()
        return member.hasPermission(ManagePortal, self.context)

    
    __call__ = ViewPageTemplateFile('portletpage.pt')
