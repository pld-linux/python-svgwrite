#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		svgwrite
%define		egg_name	svgwrite
%define		pypi_name	svgwrite
Summary:	Python 2 library to create SVG drawings
Name:		python-%{pypi_name}
Version:	1.3.1
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/mozman/svgwrite/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	a3d9311578538ba5acd6bb98d14cae38
URL:		https://github.com/mozman/svgwrite
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-pyparsing
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-pyparsing
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 library to create SVG drawings.

%package -n python3-%{pypi_name}
Summary:	Python 3 library to create SVG drawings
Requires:	python3-pyparsing
Requires:	python3-setuptools

%description -n python3-%{pypi_name}
Python 3 library to create SVG drawings.

%prep
%setup -q -n %{pypi_name}-%{version}

# test is hosed and fails on the order of attr in a tag
%{__rm} tests/test_pretty_xml.py
# needs network access
%{__rm} tests/test_style.py

%build
%py3_build
%py_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%{__python} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py3_install
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS.rst README.rst LICENSE.TXT
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py%{py_ver}.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc NEWS.rst README.rst LICENSE.TXT
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{pypi_name}-%{version}-py%{py3_ver}.egg-info
%endif
