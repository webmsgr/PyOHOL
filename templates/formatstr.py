
importstr = {"sys":(lambda imp: f"cdef extern from '<{imp}>':\n    pass\n"),
             "outside":(lambda imp: f"cdef extern from '{imp}':\n"),
             "inside":(lambda imp: f"from {imp} cimport *\n")
            }
func = {"pxd":{
        "cdef":(lambda func,args: f"cdef {func.return_type} {func.name} ({args})\n"),
        "nocdef":(lambda func,args: f"{func.return_type} {func.name} ({args})\n")
        }}
argument = lambda arg: f"{str(arg.decl_type).replace(' * * ',' ** ').replace(' * ',' *')} {arg.name}"

