%define	upstream_name	 File-Cache
%define	upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/~dclinton/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCLINTON/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chmod 755 $RPM_BUILD_ROOT%{perl_vendorlib}/File/Cache.pm

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README TODO
%{perl_vendorlib}/File/Cache.pm
%{_mandir}/man3/*
