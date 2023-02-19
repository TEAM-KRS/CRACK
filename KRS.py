import os, sys, platform


try:
    if sys.argv[1]=='update':
        os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')
except:
    pass
os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')
os.system('git pull')
os.system('clear')
os.system('\033[1;91mTOOLS\033[1;92mOFF')
