
# @todo completly rewrite the entirely of make.py

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import os
import py_decl
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
    global_namespace = py_decl.namespace(global_namespace)
    global_namespace.parse()
    return global_namespace
