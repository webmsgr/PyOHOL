# contains classes that represent decls in cpp/h files
class Base():
    def __init__(self,data,indent):
        self.type = ""
        self.data = data
        self.namespaces = []
        self.functions = []
        self.varables = []
        self.classes = []
        self.props = []
        self.indent = indent*4
        self.indentlevel = indent
        self.name = self.data.name
    def all(self):
        return self.namespaces+self.functions+self.classes+self.props+self.varables
    def _children(self): # takes self.data and populates all other properties
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
        try:
            funcs = self.data.calldefs()
        except:
            funcs = []
        for f in funcs:
            if not f.is_artificial:
                self.functions.append(func(f,self.indentlevel+1))
        try:
            vas = self.data.variables()
        except:
            vas = []
        for var in vas:
            if not var.is_artificial:
                self.varables.append(variable(var,self.indentlevel+1))
    def _parseChildren(self,rec=True):
        for clas in self.classes:
            clas.parse(False,rec)
        for anamespace in self.namespaces:
            anamespace.parse(False,rec)
        for funcs in self.functions:
            funcs.parse(False,rec)
        for var in self.varables:
            var.parse(False,rec)
        return
    def toPYX(self,recurse=False):
        return ""
    def toPXD(self,recurse=False):
        return ""
    def parse(self,recurseFirst=False,recurse=True):
        self._children() # populate self
        if recurse:
            self._parseChildren(not recurseFirst) # parse children
class FileContents():
    def __init__(self,name,filename):
        self.type = "file"
        self.name = filename
        self.indent = 0
        self.ns = name
        self.namespaces = [name]
        self.fl = filename
        self.data = name.data
        self.classes = [x for x in self.ns.classes if filename in x.data.location.file_name]
        self.functions = [x for x in self.ns.functions if filename in x.data.location.file_name]
    def all(self):
        return self.classes+self.namespaces+self.classes
def convertns(ns):
    out = []
    ufiles = list(set([x.data.location.file_name for x in ns.all() if x.data.location]))
    for file in ufiles:
        out.append(FileContents(ns,file))
    return out
class namespace(Base):
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "namespace"
class func(Base): # function
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "function"
class cppclass(Base):
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "cppclass"
class include(Base):
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "include"
class prop(Base): # property
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "property"
class variable(Base):
    def __init__(self,data,indent):
        super().__init__(data,indent)
        self.type = "variable"
