#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MLDBM
%define		pnam	MLDBM-Sync
Summary:	MLDBM - store multi-level hash structure in single level tied hash Sync
Summary(pl):	MLDBM - przechowywanie wielopoziomowej struktury haszy w jednopoziomowym haszu zwi±zanym Sync
Name:		perl-MLDBM-Sync
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb4e8d4bd6a30eee3f1126956409321
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-MLDBM
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDBM Perl module can serve as a transparent interface to any TIEHASH
package that is required to store arbitrary perl data, including
nested references. Thus, this module can be used for storing
references and other arbitrary data within DBM databases.

%description
Modu³ Perla MLDBM mo¿e s³u¿yæ za przezroczysty interfejs do dowolnego
pakietu TIEHASH, od którego wymaga siê przechowywania dowolnych danych
perla, w³±cznie z zagnie¿d¿onymi referencjami. Zatem modu³ ten s³u¿y
do przychowywania referencji oraz innych dowolnych danych w bazach
DBM.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc CHANGES README
%{perl_vendorlib}/MLDBM/Sync.pm
%{perl_vendorlib}/MLDBM/Sync/SDBM_File.pm
%{perl_vendorlib}/MLDBM/Sync
%{_mandir}/man3/*
