#!/usr/bin/env python


import os

if __name__ == '__main__' :
    file_path = os.path.realpath(__file__)
    print("Project by HookSander (https://github.com/HookSandeer)\nStarting python script ...")
    file_path = file_path[:-17]
    current_script = str(file_path) + "Output_File/script.py"
    os.system("python3 {}".format(current_script))