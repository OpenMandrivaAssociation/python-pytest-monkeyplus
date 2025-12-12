%bcond_without tests
%global pypi_name pytest-monkeyplus
%define psnme Send2Trash 

Name:           python-pytest-monkeyplus
Version:        1.1.0
Release:        2
Summary:        pytest-monkeyplus - monkeypatch with extras

License:        MIT
URL:            https://github.com/thodnev/MonkeyTest
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         fix-requires.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%if %{with tests}
BuildRequires:  python-attrs
BuildRequires:  python-pytz
Buildrequires:  python-pytest
%endif
Requires:       python-pytest


%description
The monkeyplus plugin is a funcarg that subclasses monkeypatch and adds
a few extra features to it.
monkeyplus has three extra methods: patch_osstat, patch_today and
patch_time_ticking

%{?python_provide:%python_provide python-%{pypi_name}}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%doc README CHANGES
%{python3_sitelib}/*
