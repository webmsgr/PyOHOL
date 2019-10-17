import sys
import make
import py_decl
import os

def show(obj):
    out = obj.toLog()
    for thing in obj.all():
        out += show(thing)
    return out
sys.argv.append("OneLife/server/server.cpp")
print("deftree, showing a tree of decls in a c file")
if len(sys.argv) == 1:
    print("Usage: deftree.py <cfile>")
    sys.exit(1)
ns = make.parse_file(sys.argv[1])
try:
    os.mkdir("treeout")
except:
    pass
for n in ns:
    print("saving {0} to treeout/{0}.log".format(n.fl))
        with open("treeout/{}.log".format(n.fl),"w") as f:
            f.write(show(n))
