%include	/usr/lib/rpm/macros.python
%define		lname	newsfeed
Summary:	A reader and aggregator for RSS/RDF/Atom feeds in Python/Tk
Summary(pl.UTF-8):	Czytnik i agregator dla potoków RSS/RDF/Atom w Pythonie-Tk
Name:		NewsFeed
Version:	2.11
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://home.arcor.de/mdoege/newsfeed/%{name}-%{version}.tar.gz
# Source0-md5:	49bbd9e5798f734f91992d017233b3a2
Source1:	%{lname}.desktop
Source2:	%{lname}.png
BuildRequires:	rpmbuild(macros) >= 1.231
BuildRequires:	rpm-pythonprov
Requires:	python-tkinter >= 2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A reader and aggregator for RSS/RDF/Atom feeds in Python/Tk

%description -l pl.UTF-8
Czytnik i agregator dla potoków RSS/RDF/Atom w Pythonie-Tk.

%prep
%setup -q
# fix sounds path
%{__sed} -i -e 's,/usr/X11R6/share/gnome,%{_datadir}/NewsFeed,g' newsfeed.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/NewsFeed/sounds,%{_desktopdir},%{_pixmapsdir}}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{lname}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{lname}.png
cp -f email.wav $RPM_BUILD_ROOT%{_datadir}/NewsFeed/sounds
rm -fr $RPM_BUILD_ROOT/usr/sounds

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/NewsFeed
%dir %{_datadir}/NewsFeed/sounds
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/NewsFeed-%{version}-*.egg-info
%{_datadir}/NewsFeed/sounds/email.wav
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
