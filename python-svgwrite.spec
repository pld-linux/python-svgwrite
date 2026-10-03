#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-svgwrite.spec)

%define		module		svgwrite
Summary:	Python 2 library to create SVG drawings
Summary(pl.UTF-8):	Biblioteka Pythona 2 do tworzenia rysunków SVG
Name:		python-%{module}
# keep 1.3.x here for python2 support
Version:	1.3.1
Release:	8
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/mozman/svgwrite/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	a3d9311578538ba5acd6bb98d14cae38
URL:		https://github.com/mozman/svgwrite
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pyparsing >= 2.0.1
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pyparsing >= 2.0.1
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 library to create SVG drawings.

%description -l pl.UTF-8
Biblioteka Pythona 2 do tworzenia rysunków SVG.

%package -n python3-%{module}
Summary:	Python 3 library to create SVG drawings
Summary(pl.UTF-8):	Biblioteka Pythona 3 do tworzenia rysunków SVG
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Python 3 library to create SVG drawings.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka Pythona 3 do tworzenia rysunków SVG.

%prep
%setup -q -n %{module}-%{version}

# test is hosed and fails on the order of attr in a tag
%{__rm} tests/test_pretty_xml.py
# needs network access
%{__rm} tests/test_style.py

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS.rst README.rst LICENSE.TXT
%{py_sitescriptdir}/svgwrite
%{py_sitescriptdir}/svgwrite-%{version}-py%{py_ver}.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc NEWS.rst README.rst LICENSE.TXT
%{py3_sitescriptdir}/svgwrite
%{py3_sitescriptdir}/svgwrite-%{version}-py%{py3_ver}.egg-info
%endif
