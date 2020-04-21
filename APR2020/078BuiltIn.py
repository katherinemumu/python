'''
katherinemumu
Apr 21 2020
This program will find the built in modules
'''

import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))
