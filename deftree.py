import sys
import make
import py_decl

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
ns = make.parseCpp(sys.argv[1])
ns = py_decl.convertns(ns)
for n in ns:
    if sys.argv[1] in n.fl:
        print(n.fl)
        print(show(n))
        print("saving tree to log.log")
        with open("log.log","w") as f:
            f.write(show(n))
