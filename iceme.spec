Summary:	graphical menu editor for IceWM
Name:		iceme
Version:	1.0.0
Release:	1
License:	GPL
BuildArch:	noarch
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Source0:	http://download.sourceforge.net/iceme/%{name}-%{version}.tar.gz
Patch0:		%{name}-location.patch
URL:		http://iceme.sourceforge.net
Requires:	python >= 1.5.2, pygtk >= 0.6.6
Requires:	icewm >= 0.94
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
IceMe is a graphical menu and shortcut editor for the fast and
light-weight window manager IceWM. It allows the user to edit the
IceWM menu with either drag and drop or cut and paste. If started as
root, can edit the global menu, too. This version is for IceWM 0.94 or
higher.

%prep -q
%setup -q

%patch0 -p1

%build
%{__make} BUILD_ROOT=$RPM_BUILD_ROOT

%clean
make BUILD_ROOT=$RPM_BUILD_ROOT clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} BUILD_ROOT=$RPM_BUILD_ROOT install

gzip -9nf Changelog FAQ README TODO

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/iceme
%{_prefix}/iceme
