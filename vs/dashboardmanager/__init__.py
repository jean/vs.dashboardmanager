  # -*- extra stuff goes here -*- 

import patches
from zope.i18nmessageid import MessageFactory

MF = MessageFactory('vs.dashboardmanager')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

