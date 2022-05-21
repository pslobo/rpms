# https://github.com/aquasecurity/tfsec
%global goipath         github.com/aquasecurity/tfsec
Version:                1.21.2

%gometa

%global common_description %{expand:
Security scanner for your Terraform code.}

%global golicenses      LICENSE
%global godocs

Name:           tfsec
Release:        1%{?dist}
Summary:        Security scanner for your Terraform code

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/pluto %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc example CODE_OF_CONDUCT.md rules.md SIGNING.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat May 21 2022 Pedro <rpms@plobo.net> - 1.21.2-1.fc36
- Initial package release
