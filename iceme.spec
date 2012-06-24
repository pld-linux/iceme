#
# TODO:
# - icon for desktop
# - icons location
# - libs location
Summary:	graphical menu editor for IceWM
Summary(pl):	Graficzny edytor menu dla IceWM-a
Name:		iceme
Version:	1.0.0
Release:	3
License:	GPL
BuildArch:	noarch
Group:		X11/Window Managers/Tools
Source0:	http://download.sourceforge.net/iceme/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-location.patch
URL:		http://iceme.sourceforge.net/
Requires:	python >= 1.5.2, pygtk >= 0.6.6
Requires:	icewm >= 0.94
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
IceMe is a graphical menu and shortcut editor for the fast and
light-weight window manager IceWM. It allows the user to edit the
IceWM menu with either drag and drop or cut and paste. If started as
root, can edit the global menu, too.

%description -l pl
IceMe jest graficznym programem do edycji menu oraz skr�t�w dla
IceWM-a. Pozwala u�ytkownikowi na edycj� menu poprzez wygodne GUI. Po
wystartowaniu jako root pozwala tak�e na edycj� menu globalnego.

%prep -q
%setup -q
# for further use
#%patch0 -p1

%build
%{__make} BUILD_ROOT=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

%{__make} BUILD_ROOT=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog FAQ README TODO
%attr(755,root,root) %{_bindir}/iceme
%dir /usr/lib/iceme/*
/usr/lib/iceme/pixmaps/*
%{_applnkdir}/Settings/IceWM/*
