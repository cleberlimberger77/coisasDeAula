import cx_Freeze

executables = [ cx_Freeze.Executable(script="tiroaoalvo.py", icon="midia/imagemalvo.ico") ]

cx_Freeze.setup(      
    name = "Tiro ao alvo",
    options = {"build_exe": {"packages":["pygame"],
                            "include_files":["midia"]
                             } }, executables = executables

)