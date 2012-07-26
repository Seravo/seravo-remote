#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from subprocess import *
import os

dist = setup(name='linux-tuki-etayhteys',
	version='2.1.1',
	author='Suomen Linux-tuki (Seravo Oy)',
	author_email='linux-tuki@seravo.fi',
	maintainer='Suomen Linux-tuki (Seravo Oy)',
	maintainer_email='linux-tuki@seravo.fi',
	description='Etäyhteysohjelma Linux-tuki.fi:n asiakkaille',
	long_description='Tämän ohjelman avulla Linux-tuen asiakkaan on helppo avata etäyhteys tukihenkilöä varten.',
	url='http://linux-tuki.fi/',
	download_url='http://linux-tuki.fi/etayhteys',
	license='GNU GPL',
	platforms='linux',
	scripts=['bin/linux-tuki-etayhteys'],
	data_files=[
		('share/pixmaps', ['data/lti.png']),
		('share/applications', ['data/linux-tuki-etayhteys.desktop']),
		('share/man/man1', ['data/linux-tuki-etayhteys.1']),
		]
)

#Non-documented way of getting the final directory prefix
installCmd = dist.get_command_obj(command="install_data")
installdir = installCmd.install_dir
installroot = installCmd.root

if not installroot:
	installroot = ""

if installdir:
	installdir = os.path.join(os.path.sep,
			installdir.replace(installroot, ""))

print "\nInstallation finished! You can now run linux-tuki-etayhteys by typing 'linux-tuki-etayhteys' or through your applications menu icon."
	
## To uninstall manually delete these files/folders?
