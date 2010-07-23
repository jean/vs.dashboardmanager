
from zope.component import adapts
from zope.interface import implements, Interface
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

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
    """ ATT: get hold of all roles through PAS? """
    return (('manager', 'Manager'),
            ('members', 'Members'),
            ('fakes', 'Fakers'),
            )


from collective.portletpage.content import PortletPage
PortletPage.getRoles = getRoles

