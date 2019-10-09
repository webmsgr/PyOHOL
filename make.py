

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import os
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
def generatePXD(data,out):
    o = ""
    o += funcout(data)
    o += classes(data)
    return o
def classes(data):
    return ""

def get_classes(data):
    cl = data.classes()
    for c in cl:
        if not c.is_artificial:
            yield c

def funcout(data):
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
    print("Files: {}".format(len(files)))
    for file in files:
        print("{} functions in or included by {}".format(len(files[file]),file))
    print("Includes libs {}".format(" ".join(list(sysincludes))))
    importout = ""
    for file in files:
        if os.path.basename(file) in sysincludes:
            importout += "cdef extern from <{}>:\n    pass".format(os.path.basename(file))
            continue
        else:
            if file == "":
                print(function.name)
            importout += "cdef extern from \"{}\":\n".format(file)
        for func in files[file]:
            if str(func.return_type) != "?unknown?":
                importout += "    {} {} ({})\n".format(func.return_type,func.name,','.join([str(arg.decl_type) + " " + arg.name for arg in func.arguments if str(arg.decl_type) != "?unknown?"]))
    print("functions complete!")
    return importout

def get_free_functions(names):
    for function in names.free_functions():
        if function.is_artificial == False:
            yield function

if __name__ == "__main__":
    data = parseCpp("./OneLife/server/map.h")
    generatePXD(data,"out")
