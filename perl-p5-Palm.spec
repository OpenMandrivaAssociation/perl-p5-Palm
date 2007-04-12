%define version 1.3.0
%define release %mkrel 8
%define durl http://www.cpan.org/authors/id/A/AR/ARENSB
%define rname p5-Palm
%define name perl-%{rname}

Summary: Modules for reading manipulating, and writing .pdb and .prc database
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{durl}/%{rname}-%{version}.tar.bz2
License: GPL
Group: Development/Perl
Buildrequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://www.ooblick.com/software/coldsync/
Buildarch: noarch

%description
This is p5-Palm, a set of Perl 5 modules for reading, manipulating,
and writing the .pdb and .prc database files used by PalmOS devices
such as the PalmPilot and its successors.

%prep
%setup -q -n %{rname}-1.003_000

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__perl} test.pl

%install
%{__rm} -rf $RPM_BUILD_ROOT

%makeinstall_std

%{__rm} -rf $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README TODO
%{_bindir}/*
%{perl_vendorlib}/Palm
%_mandir/man1/*
%_mandir/man3/*

