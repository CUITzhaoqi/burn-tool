# -*- coding: utf-8 -*-

import os
import sys
import subprocess

nuitka = subprocess.Popen([
                           'nuitka',
                            '--follow-imports', 'burn-tool.py',
                            '--output-dir', 'build',
                            '--verbose',
                            '--show-scons',
                            '--show-progress',
                            '--standalone',
                          ])
nuitka.wait()
print(nuitka.returncode)




