import sys

from cx_Freeze import setup, Executable

setup( name = "pathAI", version = "3.1",

       description = "pathAI",

       executables = [Executable("main.py",

                                 base = "Win32GUI")])