# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice


class ServiceObject(object):

    def __init__(self, properties):
        self.hostname = properties['host name']
        self.servicename = properties['description']
        self.check_command = properties['check command']
        self.check_command_arg = properties['check command arg']
        self.normal_check_interval = properties['normal check interval']
        self.retry_check_interval = properties['retry check interval']
        self.max_check_attempts = properties['max check attempts']
        self.active_checks_enabled = properties['active checks enabled']
        self.passive_checks_enabled = properties['passive checks enabled']
        self.state = properties['activate']

    def hostname(self):
        return self.hostname

    def servicename(self):
        return self.servicename

    def check_command(self):
        return self.check_command

    def check_command_arg(self):
        return self.check_command_arg

    def normal_check_interval(self):
        return self.normal_check_interval

    def retry_check_interval(self):
        return self.retry_check_interval

    def max_check_attempts(self):
        return self.max_check_attempts

    def active_checks_enabled(self):
        return self.active_checks_enabled

    def passive_checks_enabled(self):
        return self.passive_checks_enabled

    def state(self):
        return self.state


class Service(object):
    """
    Centreon Web Service Object
    """

    def __init__(self):
        self.webservice = Webservice.getInstance()

    def list(self):
        return self.webservice.call_clapi('show', 'SERVICE')

    def add(self, hostname, servicename, template):
        values = [hostname, servicename, template]
        return self.webservice.call_clapi('add', 'SERVICE', values)

    def delete(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('del', 'SERVICE', values)

    def setparam(self, hostname, servicename, name, value):
        values = [hostname, servicename, name, value]
        return self.webservice.call_clapi('setparam', 'SERVICE', values)

    def addhost(self):
        pass

    def sethost(self):
        pass

    def delhost(self):
        pass

    def getmacro(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getmacro', 'SERVICE', values)

    def setmacro(self, hostname, servicename, name, value, description):
        values = [hostname, servicename, name, value, description]
        return self.webservice.call_clapi('setmacro', 'SERVICE', values)

    def delmacro(self, hostname, servicename, name):
        values = [hostname, servicename, name]
        return self.webservice.call_clapi('delmacro', 'SERVICE', values)

    def setseverity(self, hostname, servicename, name):
        values = [hostname, servicename, name]
        return self.webservice.call_clapi('setseverity', 'SERVICE', values)

    def unsetseverity(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('unsetseverity', 'SERVICE', values)

    def getcontact(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontact', 'SERVICE', values)

    def addcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, contact]
        return self.webservice.call_clapi('addcontact', 'SERVICE', values)

    def setcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontact', 'SERVICE', values)

    def delcontact(self, hostname, servicename, contact):
        try:
            for i in contact:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('delcontact', 'SERVICE', values)
            return True
        except Exception:
            return False

    def getcontactgroup(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontactgroup', 'SERVICE', values)

    def setcontactgroup(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontactgroup', 'SERVICE', values)

    def delcontactgroup(self, hostname, servicename, contact):
        try:
            for i in contact:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('delcontactgroup', 'SERVICE', values)
            return True
        except Exception:
            return False

    def gettrap(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('gettrap', 'SERVICE', values)

    def addtrap(self, hostname, servicename, trap):
        values = [hostname, servicename, trap]
        return self.webservice.call_clapi('addtrap', 'SERVICE', values)

    def settrap(self, hostname, servicename, trap):
        values = [hostname, servicename, '|'.join(trap)]
        return self.webservice.call_clapi('settrap', 'SERVICE', values)

    def deltrap(self, hostname, servicename, trap):
        try:
            for i in trap:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('deltrap', 'SERVICE', values)
            return True
        except Exception:
            return False
