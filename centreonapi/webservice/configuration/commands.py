# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice


class Commands(object):

    def __init__(self):
        """
        Constructor
        """
        self.webservice = Webservice.getInstance()

    def list(self):
        """
        Get the available commands
        """
        return self.webservice.call_clapi('show', 'CMD')

    def add(self, command_name, type, command_line):
        """
        Add a new command
        :param command_name: the command name
        :param type: (check, notif, misc or discovery)
        :param command_line: System command line that will be run on execution
        """
        values = [command_name, type, command_line]
        return self.webservice.call_clapi('add', 'CMD', values)

    def delete(self, command_name):
        """
        Delete a command
        :param command_name: the command name
        """
        return self.webservice.call_clapi('del', 'CMD', command_name)

    def setparam(self, command_name, name, value):
        """
        Change a specific parameters for a command
        :param command_name: the command name
        :param name: parameters available are (name, line, type, graph, example, comment)
        :param value: the value to change
        :return:
        """
        values = [command_name, name, value]
        return self.webservice.call_clapi('setparam', 'CMD', values)
