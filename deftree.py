import sys
import make
import declPY

def show(obj):
    out = " "*obj.indent
    out += str(obj.__class__) + " " + obj.data.name + "\n"
    for thing in obj.functions+obj.namespaces+obj.classes:
        out += show(thing)
    return out
sys.argv.append("OneLife/server/server.cpp")
print("deftree, showing a tree of decls in a c file")
if len(sys.argv) == 1:
    print("Usaqge: deftree.py <cfile>")
    sys.exit(1)
dt = make.parseCpp(sys.argv[1])
ns = declPY.namespace(dt,0)
ns.parse()
print()
print(show(ns))
