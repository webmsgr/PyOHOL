# contains classes that represent decls in cpp/h files
class Base():
    def __init__(self,data,indent):
        self.data = data
        self.namespaces = []
        self.functions = []
        self.classes = []
        self.props = []
        self.indent = indent*4
        self.indentlevel = indent
    def parse(self): # takes self.data and populates all other properties
        # namespaces
        try:
            ns = self.data.namespaces()
        except:
            ns = []
        for anamespace in ns:
            self.namespaces.append(namespace(anamespace,self.indentlevel+1))
        # classes
        try:
            cl = self.data.classes()
        except:
            cl = []
        for c in cl:
            if not c.is_artificial:
                self.classes.append(cppclass(c,self.indentlevel+1))
        # end classes
        # functions
        # insert code here...
        # end functions
        # parse all!
        for clas in self.classes:
            clas.parse()
        for anamespace in self.namespaces:
            anamespace.parse()
        return
    def toPYX(self):
        return ""
    def toPXD(self):
        return ""
class namespace(Base):
    pass
class func(Base): # function
    pass
class cppclass(Base):
    pass
class include(Base):
    pass
class prop(Base): # property
    pass
class variable(Base):
    pass
