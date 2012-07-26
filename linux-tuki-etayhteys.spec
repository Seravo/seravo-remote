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
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Otto Kekäläinen (Seravo Oy) <linux-tuki@seravo.fi>
Url: http://linux-tuki.fi/

%description
Tämän ohjelman avulla Linux-tuen asiakkaan on helppo avata etäyhteys tukihenkilöä varten.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
