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
Version:	1.1.11
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/69/a5/c5edc66eb5bd9259589b3a379c8aac4084a92cad48fc688b07c1108da272/svgwrite-%{version}.zip
#Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	106f937fdaafd05945631099d0db27f2
URL:		https://bitbucket.org/mozman/svgwrite
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
