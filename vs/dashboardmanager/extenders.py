################################################################
# vs.dashboardmanager
# (C) 2010, Veit Schiele & Andreas Jung
# Published under the GNU Public Licence V 2 (GPL 2)
################################################################


import operator

from zope.component import adapts
from zope.interface import implements, Interface
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import LinesField, DisplayList, MultiSelectionWidget
from collective.portletpage.interfaces import IPortletPage


class MyLinesField(ExtensionField, LinesField):
    """ integer field """

class PortletPageExtender(object):

    adapts(IPortletPage)
    implements(ISchemaExtender)

    fields = [MyLinesField('usedForGroups',
                            default=[],
                            vocabulary='getGroups',
                            widget=MultiSelectionWidget(
                                label="Used for groups",
                                label_msgid='label_used_for_groups',
                                i18n_domain='vs.dashboardmanager',
                                ),
                             ),
            ]

    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self.fields


def getGroups(self):
    search_view = self.restrictedTraverse('@@pas_search')
    result = search_view.searchGroups()
    result = [r['title'] for r in result if not r['pluginid'] in ('auto_group', )]
    result = sorted(result)
    return DisplayList(zip(result, result))

def getUsedForGroups(self):
    return self.getField('usedForGroups').get(self)

from collective.portletpage.content import PortletPage
PortletPage.getGroups = getGroups
PortletPage.getUsedForGroups = getUsedForGroups

