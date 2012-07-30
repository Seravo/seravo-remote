%define name linux-tuki-etayhteys
%define version 2.2
%define unmangled_version 2.2
%define release 1

Summary: Etäyhteysohjelma Linux-tuki.fi:n asiakkaille
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{unmangled_version}.tar.gz
License: GNU GPL
Group: Productivity/Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%else
BuildArch: noarch
%endif

Vendor: Otto Kekäläinen (Seravo Oy) <linux-tuki@seravo.fi>
Url: http://linux-tuki.fi/
BuildRequires: python-devel
Requires: python-gtk 
Requires: x11vnc

# per distro availability checked with http://pkgs.org/
# http://lists.opensuse.org/opensuse-buildservice/2012-07/msg00097.html see this thread
# http://software.opensuse.org/search?q=x11vnc&baseproject=SUSE%3ASLE-11%3ASP1&search_devel=false&search_unsupported=false
# in this case, there's no official package in the result. so 1. add that to "BuildRequires" instead of "Requires" to 
# see if build fails, if not, there is official version available but not searchable; 2. if no official version available, 
# use "osc linkpac project packge your_project" to link it into your home project, then "osc meta pkg x11vnc -e" then 
# "<build><disable repository="openSUSE_12.1" /></build>" to disable its build


%if 0%{?suse_version}
BuildRequires: update-desktop-files
Requires: python-pexpect
%endif

%if 0%{?suse_version} > 1200
BuildRequires: python-distribute
%endif

%if 0%{?suse_version} < 1200
BuildRequires: python-setuptools
%endif

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires: python-distribute
BuildRequires: desktop-file-utils
Requires: pexpect
%endif
 
%description
Tämän ohjelman avulla Linux-tuen asiakkaan on helppo avata etäyhteys tukihenkilöä varten.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if 0%{?suse_version}
%suse_update_desktop_file -n %{name} Network
%endif

%files
%defattr(-,root,root)
/usr/bin/%{name}
/usr/share/applications/%{name}.desktop
/usr/share/man/man1/%{name}.1.gz
/usr/share/pixmaps/lti.png

%if 0%{?suse_version} && 0%{?suse_version} <= 1110
# /usr/lib/python2.6/site-packages/linux_tuki_etayhteys-2.1.1-py2.6.egg-info
#  error: Installed (but unpackaged) file(s) found:
#  /usr/lib64/python2.6/site-packages/linux_tuki_etayhteys-2.1.1-py2.6.egg-info
%python_sitearch/%{name}-%{unmangled_version}-py%{py_ver}.egg-info
# "/usr/lib64/python2.6/site-packages/linux_tuki_etayhteys-2.1.1-py2.6.egg-info" is not allowed in a noarch package.
%else

%if 0%{?rhel_version} == 600 || 0%{?centos_version} == 600
%python_sitelib/%{name}-%{unmangled_version}-py2.6.egg-info
%else
%python_sitelib/%{name}-%{unmangled_version}-py2.7.egg-info
%endif

# %py_ver does not get translated in Fedora
# %python_sitelib/linux_tuki_etayhteys-2.1.1-py%{py_ver}.egg-info
%endif
