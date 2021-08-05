'''
Created on 25 мая 2020 г.

@author: Артем
'''

import cx_Freeze
import sys

executables = [cx_Freeze.Executable("witcher.py")]
sys.argv.append('build')
cx_Freeze.setup(
    name = 'Witcher3.Wild hunt',
    options = {'Witcher3.Wild hunt': {"packages":["pygame"]}},
    executables = executables)