# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           k9s
Version:        0.25.18
Release:        1%{?dist}
Summary:        Kubernetes text-based user interface (TUI)
License:        Apache2
URL:            https://github.com/derailed/k9s
Source0:        https://github.com/derailed/%{name}/archive/v%{version}.tar.gz

# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git gzip tar

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup

%build
make build

%install
install -Dm0755 execs/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog

* Sat May 21 2022 Pedro <rpms@plobo.net> - 0.25.18-1.fc36
- chore: Initial release
