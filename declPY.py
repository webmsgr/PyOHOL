# contains classes that represent decls in cpp/h files
class Base():
    def __init__(self,data,indent):
        self.data = data
        self.functions = []
        self.classes = []
        self.props = []
        self.indent = indent*4
        self.indentlevel = indent
    def parse(self):
        pass # takes self.data and populates all other properties
    def toPYX(self):
        return ""
    def toPXD(self):
        return ""
class func(Base): # function
    pass    
class cppclass(Base):
    pass
class include(Base):
    pass
class prop(Base): # property
    pass
