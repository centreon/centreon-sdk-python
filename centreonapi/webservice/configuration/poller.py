# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice

class Poller(object):
    """
    Centreon Web poller
    """

    def __init__(self):
        """
        Constructor
        """
        self.webservice = Webservice.getInstance()

    def applycfg(self, pollername):
        """
        Apply the configuration to a poller name
        """
        return self.webservice.call_clapi('applycfg', None, pollername)

    def list(self):
        """
        list Poller
        """
        return self.webservice.call_clapi('show', 'INSTANCE')

    def show(self, pollername):
        values = [pollername]
        return self.webservice.call_clapi('show', 'INSTANCE', values)

    def get(self, pollername):
        list_pollers = self.show(pollername)
        for poller in list_pollers['result']:
            if pollername == poller['name']:
                return poller

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def setparam(self, *args, **kwargs):
        pass

    def gethosts(self, pollername):
        return self.webservice.call_clapi('gethosts', 'INSTANCE', pollername)

    def reload(self, pollername):
        """
        Reload a poller name
        """
        return self.webservice.call_clapi('pollerreload', None, pollername)

    def restart(self, pollername):
        """
        Restart a poller name
        """
        return self.webservice.call_clapi('pollerrestart', None, pollername)
