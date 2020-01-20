Name: zaf
Summary: South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release: 0.9.%{upstreamid}svn%{?dist}
Source: zaf-0-0.1.%{upstreamid}svn.tar.bz2
Group: Applications/Text
URL: http://zaf.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#zu/myspell/zu_aff.py and tools/plural-maker state unversioned GPL
License: LGPLv2+ and GPL+
BuildArch: noarch

%description
South Africa hyphenation rules.

%package -n hyphen-af
Summary: Afrikaans hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-af
Afrikaans hyphenation rules.

%package -n hyphen-zu
Summary: Zulu hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-zu
Zulu hyphenation rules.

%prep
%setup -q -n zaf

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./af/hyph/hyph_af_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./zu/hyph/hyph_zu_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s hyph_af_ZA.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files -n hyphen-af
%defattr(-,root,root,-)
%doc af/CREDITS af/COPYING af/README
%{_datadir}/hyphen/hyph_af*

%files -n hyphen-zu
%defattr(-,root,root,-)
%doc zu/CREDITS zu/COPYING zu/README
%{_datadir}/hyphen/hyph_zu*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0-0.9.20080714svn
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Caolán McNamara <caolanm@redhat.com> - 0-0.7.20080714svn
- clarify license

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20080714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Caolán McNamara <caolanm@redhat.com> - 0-0.1.20080714svn
- latest version

* Fri Nov 23 2007 Caolán McNamara <caolanm@redhat.com> - 0-0.1.20071123svn
- initial version
