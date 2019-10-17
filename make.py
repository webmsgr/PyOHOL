
# @todo completly rewrite the entirely of make.py

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import os
import py_decl
import glob
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Find the location of the xml generator (castxml or gccxml)
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(xml_generator_path=generator_path,xml_generator=generator_name)


def makeMinorGems():
    makeOne("minorGems")
def makeOneLife():
    makeOne("OneLife")
def makeOne(folder):
    incfiles = []
    for file in glob.glob(folder+"/**/*.h",recursive=True):
        try:
            incfiles += py_decl.convertns(parse_file(file))
        except RuntimeError:
            print("skipped file {} because of a error".format(file))
    files = {}
    for file in incfiles:
        if file.fl in files:
            files[file.fl].things += file.things
        else:
            files[file.fl] = file
    print("Found {} files to convert".format(len(files)))
    #for file in files:
        #print(file + ":" + str(len(files[file].things)))
    # @todo make it make the pyx/pyd combos
    # @body i cant wait
def make():
    pass
def parseCpp(file):
    return parse_file(file)
def parse_file(file):
    # Parse the c++ file
    decls = parser.parse([file], xml_generator_config)

    # Get access to the global namespace
    global_namespace = declarations.get_global_namespace(decls)
    global_namespace = py_decl.namespace(global_namespace,1)
    global_namespace.parse()
    global_namespace = py_decl.convertns(global_namespace)
    return global_namespace

if __name__ == "__main__":
    makeOneLife()
    makeMinorGems()
    make()