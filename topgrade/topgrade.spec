%global debug_package %{nil}

Name:           topgrade
Version:        9.0.0
Release:        1%{?dist}
Summary:        Topgrade - Invoke the upgrade procedure of multiple package managers

Group:          System Environment/Shells
License:        GPLv3
URL:            https://github.com/r-darwish/topgrade
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cargo

%description
Keeping your system up to date mostly involves invoking more than a single package manager. This usually results in big shell one-liners saved in your shell history. Topgrade tries to solve this problem by detecting which tools you use and run their appropriate package managers.

%prep
%autosetup

%build
cargo build

%install
install -Dm 0755 target/debug/%{name} %{buildroot}%{_bindir}/%{name}

install -Dpm0644 %{name}.8 %{buildroot}/%{_mandir}/man8/%{name}.8

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/*.8*

%changelog
* Sat May 21 2022 Pedro <rpms@plobo.net> - 9.0.0-1.fc36
- Initial release

