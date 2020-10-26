#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : conda
Version  : 4.9.1
Release  : 45
URL      : https://github.com/conda/conda/archive/4.9.1/conda-4.9.1.tar.gz
Source0  : https://github.com/conda/conda/archive/4.9.1/conda-4.9.1.tar.gz
Summary  : OS-agnostic, system-level binary package manager.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ICU ISC MIT ZPL-2.1
Requires: conda-bin = %{version}-%{release}
Requires: conda-license = %{version}-%{release}
Requires: conda-python = %{version}-%{release}
Requires: conda-python3 = %{version}-%{release}
Requires: Babel
Requires: Cython
Requires: Django
Requires: PyDispatcher
Requires: PyJWT
Requires: PySocks
Requires: appdirs
Requires: argon2-cffi
Requires: asn1crypto
Requires: attrs
Requires: bcrypt
Requires: certifi
Requires: cffi
Requires: chardet
Requires: cheroot
Requires: click
Requires: cloudpickle
Requires: cryptography
Requires: cssselect
Requires: distributed
Requires: entrypoints
Requires: flake8
Requires: flake8-import-order
Requires: git
Requires: graphviz
Requires: h5py
Requires: html5lib
Requires: idna
Requires: jaraco.functools
Requires: keyring
Requires: linecache2
Requires: lxml
Requires: more-itertools
Requires: numpy
Requires: pandas
Requires: partd
Requires: pluggy
Requires: portend
Requires: py
Requires: pyOpenSSL
Requires: pyasn1
Requires: pyasn1-modules
Requires: pycosat
Requires: pycparser
Requires: pyserial
Requires: pytz
Requires: pyxdg
Requires: requests
Requires: ruamel.yaml
Requires: secretstorage
Requires: setuptools
Requires: six
Requires: tempora
Requires: toolz
Requires: traceback2
Requires: urllib3
Requires: virtualenv
Requires: zope.interface
BuildRequires : Babel
BuildRequires : Cython
BuildRequires : Django
BuildRequires : PyDispatcher
BuildRequires : PyJWT
BuildRequires : PySocks
BuildRequires : appdirs
BuildRequires : argon2-cffi
BuildRequires : asn1crypto
BuildRequires : attrs
BuildRequires : bcrypt
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : chardet
BuildRequires : cheroot
BuildRequires : click
BuildRequires : cloudpickle
BuildRequires : cryptography
BuildRequires : cssselect
BuildRequires : distributed
BuildRequires : entrypoints
BuildRequires : flake8
BuildRequires : flake8-import-order
BuildRequires : git
BuildRequires : graphviz
BuildRequires : h5py
BuildRequires : html5lib
BuildRequires : idna
BuildRequires : jaraco.functools
BuildRequires : keyring
BuildRequires : linecache2
BuildRequires : lxml
BuildRequires : more-itertools
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : partd
BuildRequires : pluggy
BuildRequires : portend
BuildRequires : py
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pycosat
BuildRequires : pycparser
BuildRequires : pyserial
BuildRequires : pytz
BuildRequires : pyxdg
BuildRequires : requests
BuildRequires : ruamel.yaml
BuildRequires : secretstorage
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tempora
BuildRequires : toolz
BuildRequires : traceback2
BuildRequires : urllib3
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
conda.pydata.org. If you update this file, be sure to cd to the web
directory and run ``make html; make live``

%package bin
Summary: bin components for the conda package.
Group: Binaries
Requires: conda-license = %{version}-%{release}

%description bin
bin components for the conda package.


%package license
Summary: license components for the conda package.
Group: Default

%description license
license components for the conda package.


%package python
Summary: python components for the conda package.
Group: Default
Requires: conda-python3 = %{version}-%{release}

%description python
python components for the conda package.


%package python3
Summary: python3 components for the conda package.
Group: Default
Requires: python3-core
Provides: pypi(conda)
Requires: pypi(pycosat)
Requires: pypi(requests)
Requires: pypi(ruamel.yaml)

%description python3
python3 components for the conda package.


%prep
%setup -q -n conda-4.9.1
cd %{_builddir}/conda-4.9.1

%build
## build_prepend content
echo %{version} > conda/.version
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603749830
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conda
cp %{_builddir}/conda-4.9.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/5e842d4c67374b56361a282b286e4d815ff4fa5e
cp %{_builddir}/conda-4.9.1/conda/_vendor/auxlib/LICENSE %{buildroot}/usr/share/package-licenses/conda/c4a5515317f7a4fd659b36dc08ebc63536f05008
cp %{_builddir}/conda-4.9.1/conda/_vendor/boltons/LICENSE %{buildroot}/usr/share/package-licenses/conda/36a8045c70e218df3005c840a1ff4f468c440fdc
cp %{_builddir}/conda-4.9.1/conda/_vendor/toolz/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/78653a88ec8550f2d7425fac201e6fa43be4d1dd
cp %{_builddir}/conda-4.9.1/conda/_vendor/tqdm/LICENSE %{buildroot}/usr/share/package-licenses/conda/db1e38a8e85ca5af92d182028bced0a1edc37e10
cp %{_builddir}/conda-4.9.1/conda/_vendor/urllib3/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/33e6493582eea280e7c92c6803e117ae06234c01
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/Babel-2.6.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/b7507da9bfa2678a6a925d37f935bfdbbc6dd49a
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/CherryPy-17.2.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/6632ee03d13feeea3fa9d12b51edf8cf5622392a
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/Django-2.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/baf11129ce63c4eef654f39a360b31cfc7d1ac67
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/attrs-18.1.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/00ff890e8493d10b07d5d3fafa23639bb071e443
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/backports.functools_lru_cache-1.5.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/cheroot-6.4.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/6632ee03d13feeea3fa9d12b51edf8cf5622392a
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/entrypoints-0.2.3.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/conda/619bfe6da95b23329e5a9c5b4acdab24920c03bd
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/idna-2.7.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/44105cb4847b4abdd7bb445df8958aa1d27ce80f
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/jaraco.functools-1.20.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/keyring-13.2.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pluggy-0.7.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/aed3d772259a5718f5bf5107aae15fefa3a654f6
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/portend-2.3.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/py-1.6.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyOpenSSL-18.0.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyasn1-0.4.4.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/5744bc18d3a014e3bccff7630f8dd48f7732216f
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyasn1_modules-0.2.2.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/5744bc18d3a014e3bccff7630f8dd48f7732216f
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pytz-2018.5.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1e37c1e8cb0fbf6ef30642bf9e559c81fe5c331
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/requests-2.19.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/cbccb0baa382627284e486135120de86b32a27ee
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/tempora-1.13.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/urllib3-1.23.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/33e6493582eea280e7c92c6803e117ae06234c01
cp %{_builddir}/conda-4.9.1/test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/zope.interface-4.5.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/conda

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conda/00ff890e8493d10b07d5d3fafa23639bb071e443
/usr/share/package-licenses/conda/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/conda/33e6493582eea280e7c92c6803e117ae06234c01
/usr/share/package-licenses/conda/36a8045c70e218df3005c840a1ff4f468c440fdc
/usr/share/package-licenses/conda/44105cb4847b4abdd7bb445df8958aa1d27ce80f
/usr/share/package-licenses/conda/5744bc18d3a014e3bccff7630f8dd48f7732216f
/usr/share/package-licenses/conda/5e842d4c67374b56361a282b286e4d815ff4fa5e
/usr/share/package-licenses/conda/619bfe6da95b23329e5a9c5b4acdab24920c03bd
/usr/share/package-licenses/conda/6632ee03d13feeea3fa9d12b51edf8cf5622392a
/usr/share/package-licenses/conda/78653a88ec8550f2d7425fac201e6fa43be4d1dd
/usr/share/package-licenses/conda/a0b53f43aab58b46bf79ba756c50771c605ab4c5
/usr/share/package-licenses/conda/a1474494d96f6ddb3a9a0d767a09871ffc388faf
/usr/share/package-licenses/conda/a1e37c1e8cb0fbf6ef30642bf9e559c81fe5c331
/usr/share/package-licenses/conda/aed3d772259a5718f5bf5107aae15fefa3a654f6
/usr/share/package-licenses/conda/b7507da9bfa2678a6a925d37f935bfdbbc6dd49a
/usr/share/package-licenses/conda/baf11129ce63c4eef654f39a360b31cfc7d1ac67
/usr/share/package-licenses/conda/c4a5515317f7a4fd659b36dc08ebc63536f05008
/usr/share/package-licenses/conda/cbccb0baa382627284e486135120de86b32a27ee
/usr/share/package-licenses/conda/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
/usr/share/package-licenses/conda/db1e38a8e85ca5af92d182028bced0a1edc37e10

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
