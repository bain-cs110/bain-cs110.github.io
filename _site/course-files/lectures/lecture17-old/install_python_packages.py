import os
import sys

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

python_path = sys.executable
pip_install = python_path + " -m pip install "

install_input = input("What Module you want to install?: ")

print(pip_install + install_input)
os.system(pip_install+install_input)
print("Done")
restart_program()
