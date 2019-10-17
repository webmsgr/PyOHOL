
# @todo completly rewrite the entirely of make.py

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import os
import py_decl
import glob
import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Find the location of the xml generator (castxml or gccxml)
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(xml_generator_path=generator_path,xml_generator=generator_name)


def makeOne(folder,buildfolder):
    incfiles = []
    for file in glob.glob(folder+"/**/*.h",recursive=True):
        try:
            incfiles += parse_file(file)
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
    print("creating build folder")
    try:
        os.mkdir("build")
    except:
        pass
    outfolder = "build/{}".format(buildfolder)
    try:
        os.mkdir(outfolder)
    except:
        pass
    print("creating files")
    for file in files:
        data = files[file]
        if file == "":
            file = folder+"_base"
        if os.path.isabs(file):
            continue
        try:
            os.makedirs(os.path.join(outfolder+"/"+os.path.dirname(file)))
        except:
            pass
        with open(os.path.join(outfolder,file+".meta.txt"),"w") as f:
            def wr(f,dt):
                f.write(dt.toLog())
                for thing in dt.all():
                    wr(f,thing)
            wr(f,data)
        with open(os.path.join(outfolder,file.split(".")[0]+"_py.pxd"),"w") as f:
            f.write(data.toPXD())
def make(folder):
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
    folder = "build_{}".format(int(time.time()))
    makeOne("OneLife",folder)
    makeOne("minorGems",folder)
    make(folder)