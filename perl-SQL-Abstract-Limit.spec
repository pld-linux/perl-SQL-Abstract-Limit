#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define	pdir	SQL
%define	pnam	Abstract-Limit
Summary:	SQL::Abstract::Limit - portable LIMIT emulation
Summary(pl.UTF-8):	SQL::Abstract::Limit - przenośna emulacja LIMIT
Name:		perl-SQL-Abstract-Limit
Version:	0.141
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SQL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8dde39b1d7910ddf5457108c02be552
URL:		http://search.cpan.org/dist/SQL-Abstract-Limit/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-SQL-Abstract >= 1.20
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portability layer for LIMIT emulation.

%description -l pl.UTF-8
Warstwa przenośności dla emulacji LIMIT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SQL/Abstract/Limit.pm
%{_mandir}/man3/*
