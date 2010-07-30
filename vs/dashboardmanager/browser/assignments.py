################################################################
# vs.dashboardmanager
# (C) 2010, Veit Schiele & Andreas Jung
# Published under the GNU Public Licence V 2 (GPL 2)
################################################################

import demjson
import operator 

from zope.component import getUtility, getMultiAdapter
from zope.app.container.interfaces import INameChooser
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlets.interfaces import IPortletManager, IPortletAssignment, IPortletAssignmentMapping
from plone.app.portlets.utils import assignment_mapping_from_key

from vs.dashboardmanager import MF as _
from vs.dashboardmanager.logger import LOG

class Assignments(BrowserView):

    template = ViewPageTemplateFile('assignments.pt')

    def groups_for_js(self):
        """ Groups for Javascript """
        groups = self.getGroups()
        return str([group['id'] for group in groups])


    def getGroups(self): 
        """ Return PAS groups """
        search_view = self.context.restrictedTraverse('@@pas_search')
        if 'name' in self.request:
            # search by 'id' also seams to work through LDAP groups
            # instead of search by 'name'
            result = search_view.searchGroups(id=self.request.name)
        else:
            result = search_view.searchGroups()
        result = [r for r in result if not r['pluginid'] in ('auto_group',)]
        result = sorted(result, key=operator.itemgetter('title')) 
        return result


    def _get_memberids_from_request(self):
        """ Return a list of userids based on the 'group' and 'userid'
            parameters from the request.
        """

        userid = self.request.get('userid', '')
        group = self.request.get('group', '')

        gt = getToolByName(self.context, 'portal_groups')
        mt = getToolByName(self.context, 'portal_membership')

        if userid and group:
            self.context.plone_utils.addPortalMessage(u'Please specify either a member or a group - but not both', 'error')
            return self.request.response.redirect(self.context.absolute_url() + '/@@assignments')

        if not userid and not group:
            self.context.plone_utils.addPortalMessage(u'Please specify either a member or a group', 'error')
            return self.request.response.redirect(self.context.absolute_url() + '/@@assignments')

        site = getUtility(ISiteRoot)
        if userid:
            userids = [userid]
        else:
            acl = self.context.acl_users
            grp = acl.getGroupById(group)
            userids = grp.getMemberIds()

        return userids


    def push_assignment(self):
        """ Push all assignment portlet page assignment into the
            dashboard of a user or a group of users.
        """

        userids = self._get_memberids_from_request()

        dashboards_updated = dict()
        site = getUtility(ISiteRoot)
        for userid in userids:

            # iterate over all configured portlet managers (1-4) for PortletPage
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

                ids2 = [tp[0] for tp in mapping2.items()]

                # and copy over the assignments
                for id, assignment in mapping.items():
                    if not id in ids2:
                        mapping2[id] = assignment
                        LOG.info('assigned portlet %s to %s' % (id, userid))
                        dashboards_updated[userid] = True

        if dashboards_updated:
            self.context.plone_utils.addPortalMessage(u'Dashboard(s) updated for members: %s' 
                                                      % ', '.join(dashboards_updated.keys()))
        else:
            self.context.plone_utils.addPortalMessage(u'No dashboards updated')
        return self.request.response.redirect(self.context.absolute_url())


    def __call__(self, *args, **kw):
        return self.template(*args, **kw)


class ViewAssignments(Assignments):

    template = ViewPageTemplateFile('view-assignments.pt')

    def get_assignments(self):
        """ Return dashboard settings for a given group or a user """

        userids = self._get_memberids_from_request()
        site = getUtility(ISiteRoot)

        user2dash = list()
        for userid in userids:
            # iterate over the four portlet managers in each user dashboard
            dash2portlets = list()
            for i in range(1, 5):
                # get hold of the user dashboard manager
                manager_name = 'plone.dashboard%d' % i
                manager = getUtility(IPortletManager, name=manager_name)
                mapping = assignment_mapping_from_key(site, 
                                                      manager_name,
                                                      category='user', 
                                                      key=userid, 
                                                      create=True)
                portlets = list()
                for portlet_id in mapping:
                    portlets.append(dict(portlet_id=portlet_id, assignment=mapping[portlet_id]))

                dash2portlets.append(dict(manager=manager_name, portlets=portlets))
            user2dash.append(dict(userid=userid, dashboards=dash2portlets))

        return user2dash


