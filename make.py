

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import os
import templates.formatstr as formatstr
# Find the location of the xml generator (castxml or gccxml)
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(xml_generator_path=generator_path,xml_generator=generator_name)


def makeMinorGems():
    pass
def makeOneLife():
    pass
def make(folder):
    pass
def parseCpp(file):
    # Parse the c++ file
    decls = parser.parse([file], xml_generator_config)

    # Get access to the global namespace
    global_namespace = declarations.get_global_namespace(decls)
    return global_namespace
def generatePYX(data):
    pass
def generatePXD(data,filen,out):
    o = ""
    o += funcout(data,filen)
    o += classes(data)
    return o
def classes(data):
    files,sysincludes = classimport(data)
    importout = ""
    for file in files:
        if os.path.basename(file) in sysincludes:
            importout += formatstr.importstr["sys"](os.path.basename(file))
            continue
        else:
            importout += formatstr.importstr["outside"](file)
        for clas in files[file]:
            typeofclas = clas.class_type
            if typeofclas == "class":
                typeofclas = "cppclass"
            importout += "    cdef {} {}:\n".format(typeofclas,clas.name)
            for var in clas.variables():
                importout += "        {} {}".format(var.decl_type,var.name)
                if var.value:
                    importout += " = {}".format(var.value)
                importout += "\n"
    return importout

def get_classes(data):
    cl = data.classes()
    for c in cl:
        if not c.is_artificial:
            yield c
def argument_format(arg):
    return ",".join([formatstr.argument(x) for x in arg])
def function_format(func,pxd,cdef):
    d = formatstr.func
    d = d["pxd" if pxd else "pyx"]["cdef" if cdef else "nocdef"](func,argument_format(func.arguments))
    return d

def classimport(data):
    classes = get_classes(data)
    files = {}
    sysincludes = set()
    for cclass in classes:
        if "/include/" in cclass.location.file_name:
            sysincludes.add(os.path.basename(cclass.location.file_name))
        if cclass.location.file_name in files:
            files[cclass.location.file_name].append(cclass)
        else:
            files[cclass.location.file_name] = [cclass]
    return files,sysincludes

def funcimport(data):
    free_functions = get_free_functions(data)
    files = {}
    sysincludes = set()
    for function in free_functions:
        if "/include/" in function.location.file_name:
            sysincludes.add(os.path.basename(function.location.file_name))
        if function.location.file_name == "":
            continue
        if function.location.file_name in files:
            files[function.location.file_name].append(function)
        else:
            files[function.location.file_name] = [function]
    return files,sysincludes

def funcout(data,filen):
    files,sysincludes = funcimport(data)
    importout = ""
    for file in files:
        if os.path.basename(file) in sysincludes:
            importout += formatstr.importstr["sys"](os.path.basename(file))
            continue
        else:      
            importout += formatstr.importstr["outside"](file)
        for func in files[file]:
            if str(func.return_type) != "?unknown?":
                fun = function_format(func,True,False)
                importout += "    "+fun#.format(func.return_type,func.name,','.join([str(arg.decl_type) + " " + arg.name for arg in func.arguments if str(arg.decl_type) != "?unknown?"]))
    print("functions complete!")
    return importout
def get_free_functions(names):
    for function in names.free_functions():
        if function.is_artificial == False:
            yield function

if __name__ == "__main__":
    with open("out.pxd","w") as w:
        data = parseCpp("./OneLife/server/map.h")
        w.write(generatePXD(data,"map.h","out"))
