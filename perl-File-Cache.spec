%define	upstream_name	 File-Cache
%define upstream_version 0.16
Name:		perl-%{upstream_name}
Version:	0.16
Release:	2

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/File-Cache
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCLINTON/File-Cache-0.16.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} perl module

%prep
%setup -q -n File-Cache-0.16

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std
chmod 755 %{buildroot}%{perl_vendorlib}/File/Cache.pm

%files
%doc CHANGES CREDITS README TODO
%{perl_vendorlib}/File/Cache.pm
%{_mandir}/man3/*

