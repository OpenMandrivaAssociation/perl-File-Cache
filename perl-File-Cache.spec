%define	upstream_name	 File-Cache
%define	upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/~dclinton/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCLINTON/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} perl module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.16-4mdv2009.0
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

