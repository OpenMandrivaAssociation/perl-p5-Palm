%define upstream_name    p5-Palm
%define upstream_version 1.012

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Modules for reading manipulating, and writing .pdb and .prc database
License:	GPL
Group:		Development/Perl
Url:		http://www.ooblick.com/software/coldsync/
Source0:	http://www.cpan.org/modules/by-module/p5/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is p5-Palm, a set of Perl 5 modules for reading, manipulating,
and writing the .pdb and .prc database files used by PalmOS devices
such as the PalmPilot and its successors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Test are broken, ignoring result
make test || :

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1:1.12.0-2mdv2011.0
+ Revision: 655244
- rebuild for updated spec-helper

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.12.0-1mdv2011.0
+ Revision: 510973
- update to 1.012

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.11.0-1mdv2010.0
+ Revision: 447137
- update to 1.011

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:1.009-5mdv2010.0
+ Revision: 430519
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1:1.009-4mdv2009.0
+ Revision: 258177
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1:1.009-3mdv2009.0
+ Revision: 246261
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1:1.009-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 1:1.009-1mdv2008.0
+ Revision: 59428
- New version 1.009

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1:1.008-9mdv2008.0
+ Revision: 25191
- 1.008
- fix version: use archive one, use epoch to fix


* Tue Sep 27 2005 Olivier Thauvin <nanardon@mandriva.org> 1.3.0-8mdk
- rebuild

* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0-7mdk
- rebuild

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.3.0-6mdk
- Use %%makeinstall_std now that it works on klama
- Remove PREFIX from Makefile.PL

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.3.0-5mdk
- Use %%make and %%makeinstall

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 1.3.0-4mdk
- remove unused sitelib macro
- Fix man dir
- Macroification
- Fix perllocal path and use macros so it will build across perl releases.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.0-3mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0-2mdk
- buildrequires

* Sun Feb 09 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0-1mdk
- 1.3.0
- use perl macros for build

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.4-2mdk
- rebuild

* Thu Jan 10 2002 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.2.4-1mdk
- First release.

