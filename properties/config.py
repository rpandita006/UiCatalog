from configparser import ConfigParser
import os
import logging


class PropertyReader(object):

    def __init__(self):
        self.properties = {}
        self.parser = ConfigParser()
        fn = os.path.join(os.path.dirname(__file__), 'properties.INI')

        self.parser.read(fn)
        self.ws_dir = os.path.dirname(os.path.realpath(fn))
        self.properties = {section: dict(self.parser.items(section)) for section in self.parser.sections()}
        logging.info('properties read from file:' + fn + ' ' + str(self.properties))

    def get_property(self, section, key):
        return self.properties[section][key]

    def get_all_properties(self, section):
        return self.properties[section]