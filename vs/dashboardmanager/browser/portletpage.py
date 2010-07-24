from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Base(BrowserView):
    """Base class for index page views
    """

class TwoColumns(Base):
    """Default view for PortletPage """
    
    __call__ = ViewPageTemplateFile('portletpage.pt')
