%global pypi_name retrying

Name:           python-retrying
Version:        XXX
Release:        1%{?dist}
Summary:        general-purpose retrying library,

License:        ASL 2.0
URL:            https://launchpad.net/retrying
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr


%description
general-purpose retrying library,

%prep
%setup -q -n retrying-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelib}/retrying.py*
%{python_sitelib}/retrying-*.egg-info

%changelog
* Fri Aug 15 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package.
