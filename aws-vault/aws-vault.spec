# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           aws-vault
Version:        6.6.0
Release:        1%{?dist}
Summary:        A vault for securely storing and accessing AWS credentials in development environments
License:        MIT license
URL:            https://github.com/99designs/${name}
Source0:       https://github.com/99designs/${name}/archive/v%{version}.tar.gz

# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
AWS Vault is a tool to securely store and access AWS credentials in a development environment.
AWS Vault stores IAM credentials in your operating system's secure keystore and then generates temporary credentials from those to expose to your shell and applications.

%prep
%autosetup

%build
make aws-vault-linux-amd64

%install
install -Dm0755 execs/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md USAGE.md
%{_bindir}/%{name}

%changelog

* Sat May 21 2022 Pedro <rpms@plobo.net> - 6.6.0
- chore: Initial release
