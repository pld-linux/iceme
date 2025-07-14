#
# TODO:
# - icon for desktop
# - icons location
# - libs location
Summary:	Graphical menu editor for IceWM
Summary(pl.UTF-8):	Graficzny edytor menu dla IceWM-a
Name:		iceme
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/%{name}/IceMe-%{version}.tar.gz
# Source0-md5:	caa574f45386fb89589b3b71e1315410
Source1:	%{name}.desktop
Patch0:		%{name}-location.patch
URL:		http://iceme.sourceforge.net/
BuildRequires:	python-devel >= 2.1
Requires:	icewm >= 0.94
Requires:	pygtk >= 0.6.6
Requires:	python >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IceMe is a graphical menu and shortcut editor for the fast and
light-weight window manager IceWM. It allows the user to edit the
IceWM menu with either drag and drop or cut and paste. If started as
root, can edit the global menu, too.

%description -l pl.UTF-8
IceMe jest graficznym programem do edycji menu oraz skrótów dla
IceWM-a. Pozwala użytkownikowi na edycję menu poprzez wygodne GUI. Po
wystartowaniu jako root pozwala także na edycję menu globalnego.

%prep
%setup -q -n IceMe-%{version}
%patch -P0 -p0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/IceWM,%{_bindir}}

python setup.py install \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT 

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM
mv $RPM_BUILD_ROOT{%{_datadir}/iceme/iceme,%{_bindir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog FAQ README TODO
%attr(755,root,root) %{_bindir}/iceme
%dir %{_datadir}/iceme
%attr(755,root,root) %{_datadir}/iceme/*.py
%{_datadir}/iceme/pixmaps
#%{_applnkdir}/Settings/IceWM/*
