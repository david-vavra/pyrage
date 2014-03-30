__author__ = 'David Vavra'

from yapsy.IPlugin import IPlugin
from pyrage.utils import *

class URPF(IPlugin):
    def __init__(self):
        self.mode=None
        self.validModes=['strict','loose']

    def changeMode(self,mode):
        if mode.lower() not in self.validModes:
            raise ErrRequiredData(":urpf:Invalid default mode specified: '{0}'".format(
                mode
            ))
        self.mode=mode

    def parseContext(self,context,*args):
        for urpf in context.iter('urpf'):
            if 'mode' not in urpf.attrib:
                raise ErrRequiredData("No urpf mode specified. Attribute 'mode' is missing.")
            self.changeMode(urpf.attrib['mode'])



