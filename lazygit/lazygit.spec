%global debug_package %{nil}

Name:       lazygit
Version:    0.34
Release:    1%{?dist}
Summary:    Simple terminal UI for git commands

License:    MIT
URL:        https://github.com/jesseduffield/lazygit
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: git-core >= 2.0
BuildRequires: go-md2man

%description
A simple terminal UI for git commands, written in Go with the gocui library.

Rant time: You've heard it before, git is powerful, but what good is that power
when everything is so damn hard to do? Interactive rebasing requires you to edit
a goddamn TODO file in your editor? Are you kidding me? To stage part of a file
you need to use a command line program to step through each hunk and if a hunk
can't be split down any further but contains code you don't want to stage, you
have to edit an arcane patch file by hand? Are you KIDDING me?! Sometimes you
get asked to stash your changes when switching branches only to realise that
after you switch and unstash that there weren't even any conflicts and it would
have been fine to just checkout the branch directly? YOU HAVE GOT TO BE KIDDING
ME!

If you're a mere mortal like me and you're tired of hearing how powerful git is
when in your daily life it's a powerful pain in your ass, lazygit might be for
you.


%prep
%autosetup -p1


%build
go get
go build \
    -ldflags "-X main.version=%{version}" \
    -o _build/%{name}

# Man page
go-md2man -in README.md -out %{name}.1


%install
install -Dpm0755 _build/%{name} %{buildroot}%{_bindir}/%{name}

# Man page
install -Dpm0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/%{name}
%{_mandir}/man1/*.1*


%changelog
* Sat May 21 2022 Pedro <rpms@plobo.net> - 0.34-1.fc36
- Initial Release
