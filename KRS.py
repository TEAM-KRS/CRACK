#coding=utf-8

import os, sys, platform

os.system('xdg-open https://www.facebook.com/100094715435173/posts/139093385924509/?substory_index=1052463272834228&app=fbl/')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')

except:

    pass

os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('KRS64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/KRS64.cpython-311.so > KRS64.cpython-311.so') 

        os.system("chmod 777 KRS64*")
        
        import KRS64

    else:

        import KRS64

elif bit == '32bit':

    if not os.path.isfile('KRS32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/KRS32.cpython-311.so > KRS32.cpython-311.so')

        os.system("chmod 777 KRS32*")

        import KRS32

    else:

        import KRS32
        os.system("clear")
