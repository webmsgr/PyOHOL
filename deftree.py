import sys
import make
import declPY

def show(obj):
    out = " "*obj.indent
    out += obj.data.name
    return out

print("deftree, showing a tree of decls in a c file")
if len(sys.argv) == 1:
    print("Usaqge: deftree.py <cfile>")
    sys.exit(1)
dt = make.parseCpp(sys.argv[1])
ns = declPY.namespace(dt,0)
ns.parse()
for thing in ns.functions+ns.classes:
    print(show(thing))
