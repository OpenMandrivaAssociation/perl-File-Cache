%define	upstream_name	 File-Cache
Name:		perl-%{upstream_name}
Version:	0.16
Release:	6

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/File-Cache
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCLINTON/File-Cache-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} perl module

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
chmod 755 %{buildroot}%{perl_vendorlib}/File/Cache.pm

%files
%doc CHANGES CREDITS README TODO
%{perl_vendorlib}/File/Cache.pm
%{_mandir}/man3/*

%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 409016
- rebuild using %0.16 Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.16-4mdv2009.0
+ Revision: 241214
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-2mdv2008.0
+ Revision: 86391
- rebuild


* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.16-1mdk
- initial Mandriva release

