%define	module	File-Cache
%define	name	perl-%{module}
%define	version	0.16
%define	release	%mkrel 2

Name:		%{name}
Summary:	%{module} module for perl
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/~dclinton/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCLINTON/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{module} perl module

%prep
%setup -q -n %{module}-%{version}

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

