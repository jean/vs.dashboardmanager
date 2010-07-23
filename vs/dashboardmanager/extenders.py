
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

    fields = [MyLinesField('usedForRoles',
                            default=[],
                            vocabulary='getRoles',
                            widget=MultiSelectionWidget(
                                label="Used for roles",
                                label_msgid='used_for_roles',
                                i18n_domain='vs.dashboardmanager',
                                ),
                             ),
            ]

    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self.fields


def getRoles(self):
    """ return system-wide roles """
    mt = getToolByName(self, 'portal_membership')
    roles = sorted([r for r in mt.getPortalRoles() if r != 'Owner'])
    return zip(roles, roles)

from collective.portletpage.content import PortletPage
PortletPage.getRoles = getRoles

