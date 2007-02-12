%include	/usr/lib/rpm/macros.python
%define		lname	newsfeed
Summary:	A reader and aggregator for RSS/RDF/Atom feeds in Python/Tk
Summary(pl.UTF-8):	Czytnik i agregator dla potoków RSS/RDF/Atom w Pythonie-Tk
Name:		NewsFeed
Version:	2.5
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://home.arcor.de/mdoege/newsfeed/%{name}-%{version}.tar.gz
# Source0-md5:	6a38749ce995b2462ac47bb4307f9be3
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{lname}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{lname}.png

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*.py[co]
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
