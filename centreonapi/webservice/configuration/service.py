# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice

class Service(object):
    """
    Centreon Web Service Object
    """

    def __init__(self):
        self.webservice = Webservice.getInstance()
        self.clapi_object = 'SERVICE'

    def list(self):
        return self.webservice.call_clapi('show', self.clapi_object)

    def add(self, hostname, servicename, template):
        values = [hostname, servicename, template]
        return self.webservice.call_clapi('add', self.clapi_object, values)

    def delete(self, hostname, servicename):
        return self.webservice.call_clapi('del', self.clapi_object, [hostname, servicename])

    def setparam(self, hostname, servicename, name, value):
        values = [hostname, servicename, name, value]
        return self.webservice.call_clapi('setparam', self.clapi_object, values)

    def addhost(self):
        pass

    def sethost(self):
        pass

    def delhost(self):
        pass

    def getmacro(self, hostname, servicename):
        return self.webservice.call_clapi('getmacro', self.clapi_object, [hostname,servicename])

    def setmacro(self, hostname, servicename, name, value, description):
        values = [hostname, servicename, name, value, description]
        return self.webservice.call_clapi('setmacro', self.clapi_object, values)

    def delmacro(self, hostname, servicename, name):
        values = [hostname, servicename, name ]
        return self.webservice.call_clapi('delmacro', self.clapi_object, values)

    def setseverity(self, hostname, servicename, name):
        values = [hostname, servicename, name ]
        return self.webservice.call_clapi('setseverity', self.clapi_object, values)

    def unsetseverity(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('unsetseverity', self.clapi_object, values)

    def getcontact(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontact', self.clapi_object, values)

    def addcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, contact]
        return self.webservice.call_clapi('addcontact', self.clapi_object, values)

    def setcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontact', self.clapi_object, values)

    def delcontact(self, hostname, servicename, contact):
        try:
            for i in contact:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('delcontact', self.clapi_object, values)
            return True
        except Exception:
            return False

    def getcontactgroup(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontactgroup', self.clapi_object, values)

    def setcontactgroup(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontactgroup', self.clapi_object, values)

    def delcontactgroup(self, hostname, servicename, contact):
        try:
            for i in contact:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('delcontactgroup', self.clapi_object, values)
            return True
        except Exception:
            return False

    def gettrap(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('gettrap', self.clapi_object, values)

    def addtrap(self, hostname, servicename, trap):
        values = [hostname, servicename, trap]
        return self.webservice.call_clapi('addtrap', self.clapi_object, values)

    def settrap(self, hostname, servicename, trap):
        values = [hostname, servicename, '|'.join(trap)]
        return self.webservice.call_clapi('settrap', self.clapi_object, values)

    def deltrap(self, hostname, servicename, trap):
        try:
            for i in trap:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('deltrap', self.clapi_object, values)
            return True
        except Exception:
            return False
