Summary:	graphical menu editor for IceWM
Name:		iceme
Version:	1.0.0
Release:	1
License:	GPL
BuildArch:	noarch
Group:		X11/Window Managers
Source:		http://download.sourceforge.net/iceme/%{name}-%{version}.tar.gz
URL:		http://iceme.sourceforge.net
Requires:	python >= 1.5.2, pygtk >= 0.6.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
IceMe is a graphical menu and shortcut editor for the fast
and light-weight window manager IceWM. It allows the user
to edit the IceWM menu with either drag and drop or cut
and paste. If started as root, can edit the global menu,
too. This version is for IceWM 0.94 or higher.

%prep
%setup

%build
make BUILD_ROOT=$RPM_BUILD_ROOT

%clean
make BUILD_ROOT=$RPM_BUILD_ROOT clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make BUILD_ROOT=$RPM_BUILD_ROOT install

gzip -9nf Changelog FAQ README TODO

%files
%doc *.gz
/usr/X11R6/bin/iceme
/usr/lib/iceme
