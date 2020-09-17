import sys
import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

print(plugin_path)

def setup_envs():
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Lib', 'site-packages'))
    sys.path.append(py_site_path)
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Scripts'))
    sys.path.append(py_site_path)
    py_site_path = os.path.abspath(os.path.join(os.path.curdir, 'amd64', 'Lib'))
    sys.path.append(py_site_path)


# setup_envs()
import main

main.enter_point()
