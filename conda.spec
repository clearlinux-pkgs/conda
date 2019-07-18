#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : conda
Version  : 4.7.8
Release  : 25
URL      : https://github.com/conda/conda/archive/4.7.8/conda-4.7.8.tar.gz
Source0  : https://github.com/conda/conda/archive/4.7.8/conda-4.7.8.tar.gz
Summary  : No detailed summary available
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
Requires: asn1crypto
Requires: attrs
Requires: bcrypt
Requires: certifi
Requires: cffi
Requires: chardet
Requires: cheroot
Requires: click
Requires: cloudpickle
Requires: configparser
Requires: cryptography
Requires: cssselect
Requires: distributed
Requires: entrypoints
Requires: enum34
Requires: flake8
Requires: flake8-import-order
Requires: functools32
Requires: git
Requires: graphviz
Requires: h5py
Requires: html5lib
Requires: idna
Requires: ipaddress
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
BuildRequires : configparser
BuildRequires : cryptography
BuildRequires : cssselect
BuildRequires : distributed
BuildRequires : entrypoints
BuildRequires : enum34
BuildRequires : flake8
BuildRequires : flake8-import-order
BuildRequires : functools32
BuildRequires : git
BuildRequires : graphviz
BuildRequires : h5py
BuildRequires : html5lib
BuildRequires : idna
BuildRequires : ipaddress
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
conda.common
------------
Code in ``conda.common`` is not conda-specific.  Technically, it sits *aside* the application
stack and not *within* the stack.  It is able to stand independently on its own.
The *only* allowed imports of conda code in ``conda.common`` modules are imports of other
``conda.common`` modules and imports from ``conda._vendor``.

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

%description python3
python3 components for the conda package.


%prep
%setup -q -n conda-4.7.8

%build
## build_prepend content
echo %{version} > conda/.version
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563420605
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conda
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/LICENSE.txt
cp conda/_vendor/auxlib/LICENSE %{buildroot}/usr/share/package-licenses/conda/conda__vendor_auxlib_LICENSE
cp conda/_vendor/boltons/LICENSE %{buildroot}/usr/share/package-licenses/conda/conda__vendor_boltons_LICENSE
cp conda/_vendor/toolz/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/conda__vendor_toolz_LICENSE.txt
cp conda/_vendor/tqdm/LICENSE %{buildroot}/usr/share/package-licenses/conda/conda__vendor_tqdm_LICENSE
cp conda/_vendor/urllib3/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/conda__vendor_urllib3_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/Babel-2.6.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_Babel-2.6.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/CherryPy-17.2.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_CherryPy-17.2.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/Django-2.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_Django-2.1.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/attrs-18.1.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_attrs-18.1.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/backports.functools_lru_cache-1.5.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_backports.functools_lru_cache-1.5.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/cheroot-6.4.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_cheroot-6.4.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/entrypoints-0.2.3.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_entrypoints-0.2.3.dist-info_LICENSE
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/idna-2.7.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_idna-2.7.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/jaraco.functools-1.20.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_jaraco.functools-1.20.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/keyring-13.2.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_keyring-13.2.1.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pluggy-0.7.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pluggy-0.7.1.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/portend-2.3.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_portend-2.3.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/py-1.6.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_py-1.6.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyOpenSSL-18.0.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyOpenSSL-18.0.0.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyasn1-0.4.4.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyasn1-0.4.4.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pyasn1_modules-0.2.2.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyasn1_modules-0.2.2.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/pytz-2018.5.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pytz-2018.5.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/requests-2.19.1.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_requests-2.19.1.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/tempora-1.13.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_tempora-1.13.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/urllib3-1.23.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_urllib3-1.23.dist-info_LICENSE.txt
cp test_data/env_metadata/py36-osx-whl/lib/python3.6/site-packages/zope.interface-4.5.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_zope.interface-4.5.0.dist-info_LICENSE.txt
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
/usr/share/package-licenses/conda/LICENSE.txt
/usr/share/package-licenses/conda/conda__vendor_auxlib_LICENSE
/usr/share/package-licenses/conda/conda__vendor_boltons_LICENSE
/usr/share/package-licenses/conda/conda__vendor_toolz_LICENSE.txt
/usr/share/package-licenses/conda/conda__vendor_tqdm_LICENSE
/usr/share/package-licenses/conda/conda__vendor_urllib3_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_Babel-2.6.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_CherryPy-17.2.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_Django-2.1.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_attrs-18.1.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_backports.functools_lru_cache-1.5.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_cheroot-6.4.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_entrypoints-0.2.3.dist-info_LICENSE
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_idna-2.7.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_jaraco.functools-1.20.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_keyring-13.2.1.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pluggy-0.7.1.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_portend-2.3.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_py-1.6.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyOpenSSL-18.0.0.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyasn1-0.4.4.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pyasn1_modules-0.2.2.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_pytz-2018.5.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_requests-2.19.1.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_tempora-1.13.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_urllib3-1.23.dist-info_LICENSE.txt
/usr/share/package-licenses/conda/test_data_env_metadata_py36-osx-whl_lib_python3.6_site-packages_zope.interface-4.5.0.dist-info_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
