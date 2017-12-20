import sys
import os
import subprocess

def _install_requirements():
	print('Installing Bloby requirements...')
	subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

def install():
	_install_requirements()

	from colorama import init as color_init
	from colorama import Fore
	color_init()

	print(Fore.GREEN + 'Bloby setup successful! Run {} to start the Bloby CLI'.format(SCRIPT_PATH))

if __name__ == '__main__':
	task = sys.argv[1]

	if task == 'install':
		install()
	elif task == 'clean':
		clean()
	else:
		print(Fore.RED + '`{}` not supported'.format(task))
