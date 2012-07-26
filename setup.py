#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2012 Otto Kekäläinen / Seravo Oy <otto.kekalainen@seravo.fi>
#
#    This file is part of seravo-remote
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
from subprocess import *
import os

dist = setup(name='linux-tuki-etayhteys',
	version='2.1.1',
	author='Otto Kekäläinen (Seravo Oy)',
	author_email='linux-tuki@seravo.fi',
	maintainer='Otto Kekäläinen (Seravo Oy)',
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
