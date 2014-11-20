# Created by pyp2rpm-1.1.0b
%global pypi_name retrying

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX{?dist}
Summary:        General-purpose retrying library in Python

License:        ASL 2.0
URL:            https://github.com/rholder/retrying
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# patches from https://github.com/redhat-openstack/retrying

#
# patches_base=v1.2.3
#

BuildArch:      noarch

BuildRequires:  python2-devel

Requires:       python-six


%description
Retrying is an Apache 2.0 licensed general-purpose retrying library,
written in Python, to simplify the task of adding retry behavior to
just about anything.


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        General-purpose retrying library in Python
BuildRequires:  python3-devel
Requires:       python3-six

%description -n python3-%{pypi_name}
Retrying is an Apache 2.0 licensed general-purpose retrying library,
written in Python, to simplify the task of adding retry behavior to
just about anything.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue Sep 16 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 1.2.3-4
- Add python3 subpackage (required for python3-tooz)

* Sat Sep 06 2014 Alan Pevec <apevec@redhat.com> - 1.2.3-3
- unbundle python-six (from hguemar)

* Mon Aug 25 2014 Alan Pevec <apevec@redhat.com> - 1.2.3-1
- Initial package.
