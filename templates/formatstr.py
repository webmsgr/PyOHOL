
importstr = {"sys":(lambda imp: f"cdef extern from '<{imp}>':{chr(10)}    pass{chr(10)}"),
             "outside":(lambda imp: "cdef extern from '{imp}':{chr(10)}"),
             "inside":(lambda imp: f"from {imp} cimport *{chr(10)}")
            }
func = {"pxd":{
        "cdef":(lambda func,args: f"cdef {func.return_type} {func.name} ({args}){chr(10)}"),
        "nocdef":(lambda func,args: f"{func.return_type} {func.name} ({args}){chr(10)}")
        }}
argument = lambda arg: f"{arg.decl_type} {arg.name}"

