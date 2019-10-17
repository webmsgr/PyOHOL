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
    os.mkdir(os.path.join("treeout",os.path.basename(sys.argv[1])))
except:
    pass
for n in ns:
    try:
        os.makedirs(os.path.join("treeout",os.path.basename(sys.argv[1]),os.path.dirname(n.fl)))
    except FileExistsError:
        pass
    if os.path.isabs(n.fl):
        continue
    print("saving {0} to treeout/{0}.log".format(n.fl))
    with open("treeout/"+os.path.basename(sys.argv[1])+"/{}.log".format(n.fl),"w") as f:
        f.write(show(n))
