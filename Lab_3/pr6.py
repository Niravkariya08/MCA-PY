import os
import sys 

print('--------Operating System Information--------')
print("Current Working Directory:", os.getcwd())
print("Current User:", os.getlogin())
print("Absolute Path of Current File:", os.path.abspath(__file__))
print("Relative Path of Current File:", os.path.relpath(__file__))


print('--------System Information--------')
print("Current Python Version:", sys.version)
print("Current Platform:", sys.platform)