#
# TODO:
# - icon for desktop
# - icons location
# - libs location

Summary:	graphical menu editor for IceWM
Summary(pl):	Graficzny edytor menu dla IceWM'a
Name:		iceme
Version:	1.0.0
Release:	1
License:	GPL
BuildArch:	noarch
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://download.sourceforge.net/iceme/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
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
root, can edit the global menu, too.

%description -l pl
IceMe jest graficznym programem do edycji menu oraz skrótów dla IceWM'a.
Pozwala u¿ytkownikowi na edycjê menu poprzez wygodne GUI. Po
wystartowaniu jako root pozwala tak¿e na edycjê menu globalnego.

%prep -q
%setup -q

# for further use
#%patch0 -p1

%build
%{__make} BUILD_ROOT=$RPM_BUILD_ROOT

%clean
make BUILD_ROOT=$RPM_BUILD_ROOT clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/
%{__make} BUILD_ROOT=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

gzip -9nf Changelog FAQ README TODO

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_prefix}/bin/iceme
#%{_prefix}/lib/iceme
%dir /usr/lib/iceme/*
%{_applnkdir}/Settings/IceWM/*
