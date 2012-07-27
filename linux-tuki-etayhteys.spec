%define name linux-tuki-etayhteys
%define version 2.1.1
%define unmangled_version 2.1.1
%define release 1

Summary: Etäyhteysohjelma Linux-tuki.fi:n asiakkaille
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GNU GPL
Group: Productivity/Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Otto Kekäläinen (Seravo Oy) <linux-tuki@seravo.fi>
Url: http://linux-tuki.fi/
BuildRequires: python-devel
BuildRequires: python-distribute
BuildRequires: update-desktop-files
Requires: python(abi) = 2.7
 
%description
Tämän ohjelman avulla Linux-tuen asiakkaan on helppo avata etäyhteys tukihenkilöä varten.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
#%%suse_update_desktop_file -n %%{name} Network

%files
%defattr(-,root,root,-)
/usr/bin/linux-tuki-etayhteys
/usr/lib/python2.7/site-packages/linux_tuki_etayhteys-2.1.1-py2.7.egg-info
/usr/share/applications/linux-tuki-etayhteys.desktop
/usr/share/man/man1/linux-tuki-etayhteys.1.gz
/usr/share/pixmaps/lti.png

