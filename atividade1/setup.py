import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "atividade1",
        version = "0.1",
        description = "Meu primeiro programa em Python",
        options = {"build_exe": build_exe_options},
        executables = [Executable("atividade1.py", base=base)])