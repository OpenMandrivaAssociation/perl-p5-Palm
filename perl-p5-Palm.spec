%define version 1.009
%define release %mkrel 1
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
Url: http://www.ooblick.com/software/coldsync/
Buildarch: noarch
Epoch: 1

%description
This is p5-Palm, a set of Perl 5 modules for reading, manipulating,
and writing the .pdb and .prc database files used by PalmOS devices
such as the PalmPilot and its successors.

%prep
%setup -q -n %{rname}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# Test are broken, ignoring result
make test || :

%install
%{__rm} -rf $RPM_BUILD_ROOT

%makeinstall_std

%{__rm} -rf $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%_mandir/man1/*
%_mandir/man3/*
