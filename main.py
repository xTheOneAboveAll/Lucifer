import os

import requests

from multiprocessing.dummy import Pool as asshole

# headers

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# logo

logo = """

██╗░░░░░██╗░░░██╗░█████╗░██╗███████╗███████╗██████╗░

██║░░░░░██║░░░██║██╔══██╗██║██╔════╝██╔════╝██╔══██╗

██║░░░░░██║░░░██║██║░░╚═╝██║█████╗░░█████╗░░██████╔╝

██║░░░░░██║░░░██║██║░░██╗██║██╔══╝░░██╔══╝░░██╔══██╗

███████╗╚██████╔╝╚█████╔╝██║██║░░░░░███████╗██║░░██║

╚══════╝░╚═════╝░░╚════╝░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

                 SHELL FINDER FOR LAZY PEOPLE

                 AUTHOR: XTHEONEABOVEALL

                 VERSION: 0.1

                 

"""

# shell identifier

# if you are not satisfied you can add more

findme = ['<option value="chmod">Chmod</option>','<font color="green">-rw-r--r--</font>','root@indoxploit', '<script src="https://leafmailer.pw/style2.js"></script>','<link href="http://solevisible.com/images/alfamini.png" rel="icon" type="image/x-icon"/>','<a href='' name=\'edit\'><img src="http://solevisible.com/icons/menu/edit.svg"> Edit</a>','<input type="submit" name="submit" value="Crack"/>']

# shell path

# you can add more path if you want :D

paths = ['/','/blog/','/old/','/blog/old/','/old/blog/','/wp-admin/','/wp-content/','/admin/','/administrator/','/home/','/wp-content/plugin/','/temp/','/cgi-bin/','/download/','/uploads/']

#shell name

# add more name if you want

sname = ['shell.php','wso.php','a.php','xxx.php','alfa.php','indo.php']

# clear func

def clear():

	if os.name == 'nt':		os.system('cls')

	else:

		os.system('clear')

# check mark

def who(url):

	try:

		data = requests.get(url,headers=headers).content.decode('utf8')

		for keyword in findme:

			if keyword in data:

				return 'ok'

			else:

				pass

	except:

		pass

		

# shell finding func

def xfinder(url):

	url = url.replace('https://','').replace('http://','').replace('\n','').replace('\r','').replace('/','')

	for dir in paths:

		for snm in sname:

			payload = 'https://'+url+dir+snm

			if who(payload):

				print('\x1b[6;0;42m[ SHELL FOUND ] ➤ [ '+payload+' ] \x1b[0m')

				open('shell.txt','a').write(payload+'\n')

				return 'ok'

			else:

				print('\x1b[1;0;41m[ NOT FOUND ] ➤ [ '+payload+' ] \x1b[0m')

# using multiprocess

def prexfinder():

	clear()

	print(logo)

	try:

		urls = open(input('\x1b[2;0;36mFILE NAME  ➤ \x1b[0m'),'r+').readlines()

		pool = asshole(10)

		pool.map(xfinder, urls)

		pool.close()

		pool.join()

	except:

		prexfinder()

prexfinder()

		
