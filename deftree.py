import sys
import make
import declPY

def show(obj):
    out = " "*obj.indent
    out += str(obj.type) + " " + obj.name + "\n"
    for thing in obj.all():
        out += show(thing)
    return out
sys.argv.append("OneLife/server/server.cpp")
print("deftree, showing a tree of decls in a c file")
if len(sys.argv) == 1:
    print("Usage: deftree.py <cfile>")
    sys.exit(1)
dt = make.parseCpp(sys.argv[1])
ns = declPY.namespace(dt,1)
ns.parse()
ns = declPY.convertns(ns)
for n in ns:
    if sys.argv[1] in n.fl:
        print(n.fl)
        print(show(n))
        print("saving tree to log.log")
        with open("log.log","w") as f:
            f.write(show(n))
