import cx_Freeze
import sys
import matplotlib

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable('main.py',
               base=base,
               targetName='myApp',
               icon='resources/myicon.png')]

cx_Freeze.setup(
    name = 'SeaofBTC-Client',
    options = {'build_exe': {'packages': ['tkinter',
                                          'matplotlib'],
                             'includes': ['numpy.core._methods'],
                             'include_files': 'resources/myicon.png',
                             'bin_includes': ['zlib.so', 'libz.so']}},
    version = '0.1',
    description = 'Sea of BTC trading app',
    executables = executables
)
