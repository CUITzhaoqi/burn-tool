import sys
import os


def setup_envs():
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Lib', 'site-packages'))
    sys.path.append(py_site_path)
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Scripts'))
    sys.path.append(py_site_path)
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Lib'))
    sys.path.append(py_site_path)


setup_envs()
import main

main.enter_point()
