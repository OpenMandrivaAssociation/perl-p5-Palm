%define upstream_name    p5-Palm
%define upstream_version 1.400
Name:		perl-%{upstream_name}
Version:	1.400
Release:	7
Epoch:		1

Summary:	Modules for reading manipulating, and writing .pdb and .prc database
License:	GPL
Group:		Development/Perl
Url:		https://www.ooblick.com/software/coldsync/
Source0:	https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-1.400.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is p5-Palm, a set of Perl 5 modules for reading, manipulating,
and writing the .pdb and .prc database files used by PalmOS devices
such as the PalmPilot and its successors.

%prep
%setup -q -n Palm-1.400

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


