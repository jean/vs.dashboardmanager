from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ManagementView(BrowserView):

    template = ViewPageTemplateFile('management.pt')

    def foo(self):
        return 'bar'

    def __call__(self, *args, **kw):
        return self.template(*args, **kw)
