from Base.BaseElementEnmu import Element
from Base.BaseFile import BaseFile


class BaseInit(object):
    def __init__(self):
        self.bf = BaseFile()

    def mk_file(self):
        self.__destroy()
        self.bf.mk_file(Element.INFO_FILE)

    def __destroy(self):
        self.bf.remove_file(Element.INFO_FILE)
