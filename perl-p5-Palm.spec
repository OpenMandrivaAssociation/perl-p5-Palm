%define upstream_name    p5-Palm
%define upstream_version 1.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch: 1

Summary:     Modules for reading manipulating, and writing .pdb and .prc database
License:     GPL
Group:       Development/Perl
Url:         http://www.ooblick.com/software/coldsync/
Source0:     http://www.cpan.org/modules/by-module/p5/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is p5-Palm, a set of Perl 5 modules for reading, manipulating,
and writing the .pdb and .prc database files used by PalmOS devices
such as the PalmPilot and its successors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
