#
# TODO:
# - icon for desktop
# - icons location
# - libs location
Summary:	Graphical menu editor for IceWM
Summary(pl):	Graficzny edytor menu dla IceWM-a
Name:		iceme
Version:	1.0.0
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	23af1108032570ffa3d92480a5de39fd
Source1:	%{name}.desktop
Patch0:		%{name}-location.patch
URL:		http://iceme.sourceforge.net/
Requires:	icewm >= 0.94
Requires:	pygtk >= 0.6.6
Requires:	python >= 1.5.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IceMe is a graphical menu and shortcut editor for the fast and
light-weight window manager IceWM. It allows the user to edit the
IceWM menu with either drag and drop or cut and paste. If started as
root, can edit the global menu, too.

%description -l pl
IceMe jest graficznym programem do edycji menu oraz skrótów dla
IceWM-a. Pozwala u¿ytkownikowi na edycjê menu poprzez wygodne GUI. Po
wystartowaniu jako root pozwala tak¿e na edycjê menu globalnego.

%prep -q
%setup -q
# for further use
#%patch0 -p1

%build
%{__make} \
	BUILD_ROOT=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM

%{__make} install \
	BUILD_ROOT=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog FAQ README TODO
%attr(755,root,root) %{_bindir}/iceme
%dir %{_libdir}/iceme/*
%{_libdir}/iceme/pixmaps/*
%{_applnkdir}/Settings/IceWM/*
