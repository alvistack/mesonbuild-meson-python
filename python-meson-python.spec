# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-meson-python
Epoch: 100
Version: 0.13.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Meson Python build backend (PEP 517)
License: MIT
URL: https://github.com/mesonbuild/meson-python/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python build backend (PEP 517) for Meson projects.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-meson-python
Summary: Meson Python build backend (PEP 517)
Requires: meson >= 0.63.0
Requires: ninja-build
Requires: python3
Requires: python3-pyproject-metadata >= 0.6.1
Requires: python3-setuptools >= 60.0
Requires: python3-tomli >= 1.0.0
Provides: python3-meson-python = %{epoch}:%{version}-%{release}
Provides: python3dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson-python) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-meson-python
Python build backend (PEP 517) for Meson projects.

%files -n python%{python3_version_nodots}-meson-python
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-meson-python
Summary: Meson Python build backend (PEP 517)
Requires: meson >= 0.63.0
Requires: ninja-build
Requires: python3
Requires: python3-pyproject-metadata >= 0.6.1
Requires: python3-setuptools >= 60.0
Requires: python3-tomli >= 1.0.0
Provides: python3-meson-python = %{epoch}:%{version}-%{release}
Provides: python3dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson-python) = %{epoch}:%{version}-%{release}

%description -n python3-meson-python
Python build backend (PEP 517) for Meson projects.

%files -n python3-meson-python
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-meson-python
Summary: Meson Python build backend (PEP 517)
Requires: meson >= 0.63.0
Requires: ninja-build
Requires: python3
Requires: python3-pyproject-metadata >= 0.6.1
Requires: python3-setuptools >= 60.0
Requires: python3-tomli >= 1.0.0
Provides: python3-meson-python = %{epoch}:%{version}-%{release}
Provides: python3dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson-python) = %{epoch}:%{version}-%{release}

%description -n python3-meson-python
Python build backend (PEP 517) for Meson projects.

%files -n python3-meson-python
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
