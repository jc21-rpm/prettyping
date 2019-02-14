%global debug_package %{nil}

Name:           prettyping
Version:        1.0.1
Release:        1%{?dist}
Summary:        prettyping is a wrapper around the standard ping tool, making the output prettier, more colorful, more compact, and easier to read.
License:        MIT
URL:            https://github.com/denilsonsa/%{name}
BuildArch:      noarch
Requires:       bash >= 3.0

%description
prettyping is a wrapper around the standard ping tool with the objective of making
the output prettier, more colorful, more compact, and easier to read. prettyping
runs the standard ping in the background and parses its output, showing the ping
responses in a graphical way at the terminal (by using colors and Unicode characters).
prettyping is written in bash and awk, and is reported to work on many different
systems (Linux, Mac OS X, BSD…), as well as running on different versions of awk
(gawk, mawk, nawk, busybox awk).

%prep
wget https://github.com/denilsonsa/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz

%build
cd %{name}-%{version}
sed 's,/usr/bin/env bash,/bin/bash,g' -i prettyping

%install
mkdir -p %{buildroot}/usr/bin
install -m755 %{name}-%{version}/%{name} %{buildroot}/usr/bin

%files
%{_bindir}/%{name}
%doc %{name}-%{version}/README.md

%changelog
* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 1.0.1-1
- Initial spec

