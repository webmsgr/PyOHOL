
importstr = {"sys":f"cdef extern from '<{imp}>':\n    pass\n",
             "outside":f"cdef extern from '{imp}':\n",
             "inside":f"from {imp} cimport *\n"}
func = {"pxd":{
        "cdef":f"cdef {func.return_type} {func.name} ({args})\n",
        "nocdef":f"{func.return_type} {func.name} ({args})\n"
        }}
argument = f"{arg.decl_type} {arg.name}"

