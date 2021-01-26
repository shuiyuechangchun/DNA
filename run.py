#/usr/bin/python3

'''
Edited by Errors
2020-12-29 13:53:21 
'''

import os, sys, platform

if platform.system() == 'Linux':
	import pwd
	user = pwd.getpwuid(os.getuid()).pw_name

	os.system("clear")
	print("\033[1;32m\nRetrievaling ...\033[0m\n")
	if os.path.isdir('Insides'):
		if platform.machine() == 'x86_64':
			if os.path.isfile('Insides/Linux/dna'):
				os.system("chmod -R 777 Insides/Linux")
				if os.geteuid() != 0:
					os.system("sudo ./Insides/Linux/dna " + user)
				else:
					os.system("./Insides/Linux/dna " + user)
			else:
				os.system("clear")
				print("\033[1;33m\nThis program <dna> had been lost. Aborting ...\033[0m\n")
				sys.exit()
		elif platform.machine() == 'aarch64' or platform.machine() == 'armv8l':
			if os.path.isfile('Insides/Droid/dna'):
				os.system("chmod -R 777 Insides/Droid")
				if os.geteuid() != 0:
					os.system("sudo ./Insides/Droid/dna " + user)
				else:
					os.system("./Insides/Droid/dna " + user)
			else:
				os.system("clear")
				print("\033[1;33m\nThis program <dna> had been lost. Aborting ...\033[0m\n")
				sys.exit()
		else:
			os.system("clear")
			print("\033[1;33m\nThe platform <" + platform.machine() + "> not suppost! Aborting ...\033[0m\n")
			sys.exit(0)
	else:
		os.system("clear")
		print("\033[1;33m\nThis program <Insides> had been lost. Aborting ...\033[0m\n")
		sys.exit(1)
else:
	os.system("clear")
	print("\033[1;31m\nThis program must be run on linux. Aborting ...\033[0m\n")
	sys.exit(2)
