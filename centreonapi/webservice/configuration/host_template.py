# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice
from centreonapi.webservice.configuration.host import *

class HostTemplateObj(HostObj):
    pass

class HostTemplate(Host):
    """
    Centreon Web host object
    """

    def __init__(self):
        """
        Constructor
        """
        self.webservice = Webservice.getInstance()
        self.clapi_object = 'HTPL'

    def add(self, hostname, hostalias, hostip, hosttemplate, pollername=None, hgname=None):
        """
        Add a host template
        """
        return super(HostTemplate, self).add(hostname, hostalias, hostip, hosttemplate, '', [])

    def setinstance(self, hostname, instance):
        pass

    def applytemplate(self, hostname):
        pass

    def getparent(self, hostname):
        pass

    def addparent(self, hostname, parents):
        pass

    def setparent(self, hostname, parents):
        pass

    def deleteparent(self, hostname, parents):
        pass

    def gethostgroup(self, hostname):
        pass

    def addhostgroup(self, hostname, hostgroups):
        pass

    def sethostgroup(self, hostname, hostgroups):
        pass

    def deletehostgroup(self, hostname, hostgroups):
        pass
