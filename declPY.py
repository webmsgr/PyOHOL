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
        # classes
        cl = self.data.classes()
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
        return # takes self.data and populates all other properties
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
