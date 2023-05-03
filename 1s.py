try:

	import os,requests,json,time,re,random,sys,uuid,string,base64,zlib,hashlib,subprocess	from string import *

	from concurrent.futures import ThreadPoolExecutor as tred

except ModuleNotFoundError: 

	print('\n Installing missing modules ...')

	os.system('pip install requests futures bs4==2 > /dev/null')

	exit(' Module install done run again ')

oks,cps,loop,pcp=[],[],0,[]

logo = '''

\033[1;37m  d888888b .d8888.db       .d8b.  .88b  d88.

   `88'   88'  YP 88      d8' `8b 88'YbdP`88

    88    `8bo.   88      88ooo88 88  88  88

    88      `Y8b. 88      88~~~88 88  88  88

   .88.   db   8D 88booo. 88   88 88  88  88

 Y888888P `8888Y' Y88888P YP   YP YP  YP  YP

------------------------------------------------

  Author : SOHAIB AHMAD

  Github : Unknown

  Fcbook : Not Found

------------------------------------------------

 Nothing is impossible : just try to do

------------------------------------------------'''

def clear():

    os.system('clear')

    print(logo)

def linex():

    print('\033[1;37m----------------------------------------------')

def main():

    clear()

    print(' [1] Start File Clone \n [0] Exit Menu ');linex()

    x = input(' Choose: ')

    if x =='1':

        file()

    else:exit()

def file():

	clear()

	file = input(' Put file path\033[1;37m: ')

	try:

		fo = open(file,'r').read().splitlines()

	except FileNotFoundError:

		print(' File location not found ')

		time.sleep(1)

		main()

	clear()

	plist=[]

	try:

		ps_limit = int(input(' How many passwords do you want 
