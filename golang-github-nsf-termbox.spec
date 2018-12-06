# Run tests in check section
%bcond_without check

%global goipath         github.com/nsf/termbox-go
%global commit          5c94acc5e6eb520f1bcd183974e01171cc4c23b3

%global common_description %{expand:
A minimalistic API which allows programmers to write text-based user interfaces.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.5%{?dist}
Summary: A minimalistic API which allows programmers to write text-based user interfaces
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/mattn/go-runewidth)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-nsf-termbox-go-devel = %{version}-%{release}
Obsoletes: golang-github-nsf-termbox-go-devel < 0-0.3.20180314gite2050e4
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git5c94acc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180628git5c94acc
- Bump to commit 5c94acc5e6eb520f1bcd183974e01171cc4c23b3

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gite2050e4
- Update with the new Go packaging
- Upstream GIT revision e2050e4

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171104gitaa4a75b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171104gitaa4a75b
- Upstream GIT revision aa4a75b

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170710git4ed959e
- First package for Fedora

