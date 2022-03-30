#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Character encoding aliases for legacy web content
Summary(pl.UTF-8):	Aliasy kodowania znaków dla zastanych treści WWW
Name:		python-webencodings
Version:	0.5.1
Release:	7
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/webencodings/
Source0:	https://files.pythonhosted.org/packages/source/w/webencodings/webencodings-%{version}.tar.gz
# Source0-md5:	32f6e261d52e57bf7e1c4d41546d15b8
URL:		https://github.com/SimonSapin/python-webencodings
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%{?with_tests:BuildRequires:	python-nose}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
%{?with_tests:BuildRequires:	python3-nose}
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python 2 implementation of the WHATWG Encoding standard.

In order to be compatible with legacy web content when interpreting
something like "Content-Type: text/html; charset=latin1", tools need
to use a particular set of aliases for encoding labels as well as some
overriding rules. For example, US-ASCII and iso-8859-1 on the web are
usually aliases for windows-1252, and an UTF-8 or UTF-16 BOM takes
precedence over any other encoding declaration. The Encoding standard
defines all such details so that implementations do not have to
reverse-engineer each other.

This module has encoding labels and BOM detection, but the actual
implementation for encoders and decoders is Python's.

%description -l pl.UTF-8
Ten moduł to implementacja standardu WHATWG Encoding w Pythonie 2.

Aby być zgodnym z zastaną treścią WWW przy interpretowaniu nagłówków
typu "Content-Type: text/html; charset=latin1", narzędzia muszą użyć
pewnego zbioru aliasów oraz reguł nadpisujących. Na przykład, US-ASCII
i iso-8859-1 w sieci zwykle są aliasami dla windows-1252, a BOM UTF-8
i UTF-16 ma priorytet ponad innymi deklaracjami kodowania. Standard
Encoding definiuje wszystkie takie szczegóły, aby implementacje nie
musiały ich wynajdywać samemu.

Ten moduł zawiera etykiety kodowań oraz wykrywanie BOM; sama
implementacja kodowania i dekodowania pochodzi z Pythona.

%package -n python3-webencodings
Summary:	Character encoding aliases for legacy web content
Summary(pl.UTF-8):	Aliasy kodowania znaków dla zastanych treści WWW
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-webencodings
This is a Python 3 implementation of the WHATWG Encoding standard.

In order to be compatible with legacy web content when interpreting
something like Content-Type: text/html; charset=latin1, tools need to
use a particular set of aliases for encoding labels as well as some
overriding rules. For example, US-ASCII and iso-8859-1 on the web are
usually aliases for windows-1252, and an UTF-8 or UTF-16 BOM takes
precedence over any other encoding declaration. The Encoding standard
defines all such details so that implementations do not have to
reverse-engineer each other.

This module has encoding labels and BOM detection, but the actual
implementation for encoders and decoders is Python's.

%description -n python3-webencodings -l pl.UTF-8
Ten moduł to implementacja standardu WHATWG Encoding w Pythonie 3.

Aby być zgodnym z zastaną treścią WWW przy interpretowaniu nagłówków
typu "Content-Type: text/html; charset=latin1", narzędzia muszą użyć
pewnego zbioru aliasów oraz reguł nadpisujących. Na przykład, US-ASCII
i iso-8859-1 w sieci zwykle są aliasami dla windows-1252, a BOM UTF-8
i UTF-16 ma priorytet ponad innymi deklaracjami kodowania. Standard
Encoding definiuje wszystkie takie szczegóły, aby implementacje nie
musiały ich wynajdywać samemu.

Ten moduł zawiera etykiety kodowań oraz wykrywanie BOM; sama
implementacja kodowania i dekodowania pochodzi z Pythona.

%prep
%setup -q -n webencodings-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:nosetests-%{py_ver}}
%endif

%if %{with python3}
%py3_build

%{?with_tests:nosetests-%{py3_ver}}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/webencodings
%{py_sitescriptdir}/webencodings-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-webencodings
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/webencodings
%{py3_sitescriptdir}/webencodings-%{version}-py*.egg-info
%endif
