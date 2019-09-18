# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice

class ServiceTemplateObj(object):

    def __init__(self, properties):
        self.description = properties['description']
        self.alias = properties['alias']
        self.command = properties['check command']
        self.command_args = properties['check command arg']
        self.active = properties['active checks enabled']
        self.passive = properties['passive checks enabled']
        self.max_attempts = properties['max check attempts']
        self.interval = properties['normal check interval']
        self.retry_interval = properties['retry check interval']

    def description(self):
        return self.description

    def address(self):
        return self.address()

    def alias(self):
        return self.alias()


class ServiceTemplate(object):
    """
    Centreon Web Service Template Object
    """

    def __init__(self):
        self.webservice = Webservice.getInstance()
        self.clapi_object = 'STPL'

    def list(self):
        return self.webservice.call_clapi('show', self.clapi_object)

    def show(self, servicedescription):
        values = [servicedescription]
        return self.webservice.call_clapi('show', self.clapi_object, values)

    def get(self, servicedescription):
        list_service = self.show(servicedescription)
        for service in list_service['result']:
            if servicedescription == service['description']:
                return ServiceTemplateObj(service)

    def add(self, servicedescription, servicename, template):
        values = [servicedescription, servicename, template]
        return self.webservice.call_clapi('add', self.clapi_object, values)

    def delete(self, servicename):
        return self.webservice.call_clapi('del', self.clapi_object, [servicename])

    def setparam(self, servicename, name, value):
        values = [servicename, name, value]
        return self.webservice.call_clapi('setparam', self.clapi_object, values)

    def addhosttemplate(self, servicename, hosttemplate):
        values = [servicename, '|'.join(hosttemplate)]
        return self.webservice.call_clapi('addhosttemplate', self.clapi_object, values)

    def sethosttemplate(self, servicename, hosttemplate):
        values = [servicename, '|'.join(hosttemplate)]
        return self.webservice.call_clapi('sethosttemplate', self.clapi_object, values)

    def delhosttemplate(self, servicename, hosttemplate):
        values = [servicename, '|'.join(hosttemplate)]
        return self.webservice.call_clapi('delhosttemplate', self.clapi_object, values)

    def getmacro(self, servicename):
        return self.webservice.call_clapi('getmacro', self.clapi_object, [hostname,servicename])

    def setmacro(self, servicename, name, value, description):
        values = [servicename, name, value, description]
        return self.webservice.call_clapi('setmacro', self.clapi_object, values)

    def delmacro(self, servicename, name):
        values = [servicename, name ]
        return self.webservice.call_clapi('delmacro', self.clapi_object, values)

    def getcontact(self, servicename):
        values = [servicename]
        return self.webservice.call_clapi('getcontact', self.clapi_object, values)

    def addcontact(self, servicename, contact):
        values = [servicename, contact]
        return self.webservice.call_clapi('addcontact', self.clapi_object, values)

    def setcontact(self, servicename, contact):
        values = [servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontact', self.clapi_object, values)

    def delcontact(self, servicename, contact):
        try:
            for i in contact:
                values = [servicename, i]
                self.webservice.call_clapi('delcontact', self.clapi_object, values)
            return True
        except Exception:
            return False

    def getcontactgroup(self, servicename):
        values = [servicename]
        return self.webservice.call_clapi('getcontactgroup', self.clapi_object, values)

    def setcontactgroup(self, servicename, contact):
        values = [servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontactgroup', self.clapi_object, values)

    def delcontactgroup(self, servicename, contact):
        try:
            for i in contact:
                values = [servicename, i]
                self.webservice.call_clapi('delcontactgroup', self.clapi_object, values)
            return True
        except Exception:
            return False

    def gettrap(self, servicename):
        values = [servicename]
        return self.webservice.call_clapi('gettrap', self.clapi_object, values)

    def addtrap(self, servicename, trap):
        values = [servicename, trap]
        return self.webservice.call_clapi('addtrap', self.clapi_object, values)

    def settrap(self, servicename, trap):
        values = [servicename, '|'.join(trap)]
        return self.webservice.call_clapi('settrap', self.clapi_object, values)

    def deltrap(self, servicename, trap):
        try:
            for i in trap:
                values = [servicename, i]
                self.webservice.call_clapi('deltrap', self.clapi_object, values)
            return True
        except Exception:
            return False
