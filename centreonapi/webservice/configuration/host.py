# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice

class HostObj(object):

    def __init__(self, properties):
        self.name = properties['name']
        self.state = properties['activate']
        self.address = properties['address']
        self.alias = properties['alias']

    def name(self):
        return self.name

    def address(self):
        return self.address()

    def alias(self):
        return self.alias()

    def state(self):
        return self.state()


class Host(object):
    """
    Centreon Web host object
    """

    def __init__(self):
        """
        Constructor
        """
        self.webservice = Webservice.getInstance()
        self.clapi_object = 'HOST'

    def list(self):
        """
        List hosts
        """
        return self.webservice.call_clapi('show', self.clapi_object)

    def show(self, hostname):
        values = [hostname]
        return self.webservice.call_clapi('show', self.clapi_object, values)

    def get(self, hostname):
        list_host = self.show(hostname)
        for host in list_host['result']:
            if hostname == host['name']:
                return HostObj(host)

    def add(self, hostname, hostalias, hostip, hosttemplate, pollername, hgname):
        """
        Add a host
        """
        values = [
            hostname,
            hostalias,
            hostip,
            '|'.join(hosttemplate),
            pollername,
            '|'.join(hgname)
        ]
        return self.webservice.call_clapi('add', self.clapi_object, values)

    def delete(self, hostname):
        return self.webservice.call_clapi('del', self.clapi_object, hostname)

    def setparameters(self, hostname, name, value):
        """
        DEPRECATED
        """
        return self.setparam(hostname, name, value)

    def setparam(self, hostname, name, value):
        values = [hostname, name, value]
        return self.webservice.call_clapi('setparam', self.clapi_object, values)

    def setinstance(self, hostname, instance):
        values = [hostname, instance]
        return self.webservice.call_clapi('setinstance', self.clapi_object, values)

    def getmacro(self, hostname):
        return self.webservice.call_clapi('getmacro', self.clapi_object, hostname)

    def setmacro(self, hostname, name, value):
        values = [hostname, name, value]
        return self.webservice.call_clapi('setmacro', self.clapi_object, values)

    def deletemacro(self, hostname, name):
        values = [hostname, name]
        return self.webservice.call_clapi('delmacro', self.clapi_object, values)

    def gettemplate(self, hostname):
        return self.webservice.call_clapi('gettemplate', self.clapi_object, hostname)

    def settemplate(self, hostname, template):
        values = [hostname, "|".join(template)]
        return self.webservice.call_clapi('settemplate', self.clapi_object, values)

    def addtemplate(self, hostname, template):
        values = [hostname, "|".join(template)]
        return self.webservice.call_clapi('addtemplate', self.clapi_object, values)

    def deletetemplate(self, hostname, template):
        values = [hostname, "|".join(template)]
        return self.webservice.call_clapi('delemplate', self.clapi_object, values)

    def applytemplate(self, hostname):
        """
        Apply the host template to the host, deploy services
        """
        return self.webservice.call_clapi('applytpl', self.clapi_object, hostname)

    def getparent(self, hostname):
        return self.webservice.call_clapi('getparent', self.clapi_object, hostname)

    def addparent(self, hostname, parents):
        return self.webservice.call_clapi('addparent', self.clapi_object, [hostname, "|".join(parents)])

    def setparent(self, hostname, parents):
        return self.webservice.call_clapi('setparent', self.clapi_object, [hostname, "|".join(parents)])

    def deleteparent(self, hostname, parents):
        return self.webservice.call_clapi('delparent', self.clapi_object, [hostname, "|".join(parents)])

    def getcontactgroup(self, hostname):
        return self.webservice.call_clapi('getcontactgroup', self.clapi_object, hostname)

    def addcontactgroup(self, hostname, contactgroups):
        return self.webservice.call_clapi('addcontactgroup', self.clapi_object, [hostname, "|".join(contactgroups)])

    def setcontactgroup(self, hostname, contactgroups):
        return self.webservice.call_clapi('setcontactgroup', self.clapi_object, [hostname, "|".join(contactgroups)])

    def deletecontactgroup(self, hostname, contactgroups):
        return self.webservice.call_clapi('delcontactgroup', self.clapi_object, [hostname, "|".join(contactgroups)])

    def getcontact(self, hostname):
        return self.webservice.call_clapi('getcontact', self.clapi_object, hostname)

    def addcontact(self, hostname, contacts):
        return self.webservice.call_clapi('addcontact', self.clapi_object, [hostname, "|".join(contacts)])

    def setcontact(self, hostname, contacts):
        return self.webservice.call_clapi('setcontact', self.clapi_object, [hostname, "|".join(contacts)])

    def deletecontact(self, hostname, contacts):
        return self.webservice.call_clapi('delcontact', self.clapi_object, [hostname, "|".join(contacts)])

    def gethostgroup(self, hostname):
        return self.webservice.call_clapi('gethostgroup', self.clapi_object, hostname)

    def addhostgroup(self, hostname, hostgroups):
        return self.webservice.call_clapi('addhostgroup', self.clapi_object, [hostname, "|".join(hostgroups)])

    def sethostgroup(self, hostname, hostgroups):
        return self.webservice.call_clapi('sethostgroup', self.clapi_object, [hostname, "|".join(hostgroups)])

    def deletehostgroup(self, hostname, hostgroups):
        return self.webservice.call_clapi('delhostgroup', self.clapi_object, [hostname, "|".join(hostgroups)])

    def setseverity(self, hostname, name):
        return self.webservice.call_clapi('setseverity', self.clapi_object, [hostname, name    ])

    def unsetseverity(self, hostname):
        return self.webservice.call_clapi('unsetseverity', self.clapi_object, hostname)

    def enable(self, hostname):
        return self.webservice.call_clapi('enable', self.clapi_object, hostname)

    def disable(self, hostname):
        return self.webservice.call_clapi('disable', self.clapi_object, hostname)
