#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : repoze.sphinx.autointerface
Version  : 0.8
Release  : 3
URL      : https://files.pythonhosted.org/packages/8f/65/ea18d09c6847b3a381e16c89f26de0ddcdf0bdb8d05f4581e4df9b7033fd/repoze.sphinx.autointerface-0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/8f/65/ea18d09c6847b3a381e16c89f26de0ddcdf0bdb8d05f4581e4df9b7033fd/repoze.sphinx.autointerface-0.8.tar.gz
Source99 : https://files.pythonhosted.org/packages/8f/65/ea18d09c6847b3a381e16c89f26de0ddcdf0bdb8d05f4581e4df9b7033fd/repoze.sphinx.autointerface-0.8.tar.gz.asc
Summary  : Sphinx extension: auto-generates API docs from Zope interfaces
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.sphinx.autointerface-license = %{version}-%{release}
Requires: repoze.sphinx.autointerface-python = %{version}-%{release}
Requires: repoze.sphinx.autointerface-python3 = %{version}-%{release}
Requires: Sphinx
Requires: setuptools
Requires: zope.interface
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : zope.interface

%description
==================================
        
        Overview
        --------
        
        Thie package defines an extension for the

%package license
Summary: license components for the repoze.sphinx.autointerface package.
Group: Default

%description license
license components for the repoze.sphinx.autointerface package.


%package python
Summary: python components for the repoze.sphinx.autointerface package.
Group: Default
Requires: repoze.sphinx.autointerface-python3 = %{version}-%{release}

%description python
python components for the repoze.sphinx.autointerface package.


%package python3
Summary: python3 components for the repoze.sphinx.autointerface package.
Group: Default
Requires: python3-core

%description python3
python3 components for the repoze.sphinx.autointerface package.


%prep
%setup -q -n repoze.sphinx.autointerface-0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541278298
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/repoze.sphinx.autointerface
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/repoze.sphinx.autointerface/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/repoze.sphinx.autointerface/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
