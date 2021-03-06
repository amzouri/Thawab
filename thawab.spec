Name: thawab
Summary: Thawab Arabic/Islamic encyclopedia system
URL: http://thawab.ojuba.org/
Version: 3.0.12
Release: 1%{?dist}
Source0: http://git.ojuba.org/cgit/%{name}/snapshot/%{name}-%{version}.tar.bz2
License: Waqf
Group: System Environment/Base
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python-whoosh >= 1.7.2
Requires: python-okasha >= 0.2.3
Requires: python, mdbtools, python-paste, islamic-menus, python-othman, pygtk2, pywebkitgtk
BuildRequires: gettext
BuildRequires: python, perl

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
Thawab Arabic/Islamic encyclopedia system

%prep
%setup -q
%build
bash update-manual-from-site.sh
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE-ar.txt LICENSE-en readme
%{_bindir}/thawab-gtk
%{python_sitelib}/Thawab/*
%{python_sitelib}/*.egg-info
%{_datadir}/thawab/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/*/*.mo

%changelog
* Mon Nov 1 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.10-1
- update to whoosh 1.x.y

* Mon Jul 26 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.8-1
- activate cancel button in import window
- only reload index after new import
- css: hide overflow in minisearch

* Sun Jul 4 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.7-1
- update to latest stable release
- activate footnotes links
- opens external links with default browser
- print button
- add zoom buttons
- auto reload after import
- change search query syntax
- add manual
- add filter to book listing

* Sun Jul 4 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.5-1
- highlight minisearch text
- reload meta after import
- fix some importing bugs
- use connection-per-thread in core.py
- static-like pages

* Fri Jun 18 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.4-1
- load books from /usr/share/thawab/db/
- limit search results to 500
- notfy user for non-indexed books

* Thu Jun 17 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.3-1
- add missing Requires
- hide mini search if not indexed

* Sat Jun 12 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3.0.2-1
- initial packing

