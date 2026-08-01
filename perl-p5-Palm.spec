%define upstream_name    p5-Palm
%define real_name        Palm
%define upstream_version 1.400
Name:perl-%{upstream_name}
Version:1.400
Release:1
Epoch:1

Summary:Modules for reading manipulating, and writing .pdb and .prc database
License:GPL+ or Artistic
Group:Development/Perl
Url:https://metacpan.org/dist/Palm
Source0:https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-1.400.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:noarch

%description
This is Palm (formerly p5-Palm), a set of Perl 5 modules for reading,
manipulating, and writing the .pdb and .prc database files used by PalmOS
devices such as the PalmPilot and its successors.

%prep
%setup -q -n Palm-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%make_install
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
rm -f %{buildroot}%{perl_vendorarch}/perllocal.pod
find %{buildroot} -name .packlist -delete

%files
%doc Changes LICENSE META.yml README*
%{perl_vendorlib}/*
%{_mandir}/man3/*
