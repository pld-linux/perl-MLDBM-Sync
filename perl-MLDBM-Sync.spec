#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MLDBM
%define		pnam	Sync
Summary:	MLDBM::Sync - safe concurrent access to MLDBM databases
Summary(pl.UTF-8):	MLDBM::Sync - bezpieczny równoczesny dostęp do baz danych MLDBM
Name:		perl-MLDBM-Sync
Version:	0.30
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb4e8d4bd6a30eee3f1126956409321
URL:		http://search.cpan.org/dist/MLDBM-Sync/
BuildRequires:	perl-MLDBM
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module wraps around the MLDBM interface, by handling concurrent
access to MLDBM databases with file locking, and flushes I/O explicity
per lock/unlock. The new Lock()/UnLock() API can be used to serialize
requests logically and improve performance for bundled reads & writes.

%description -l pl.UTF-8
Ten moduł opakowuje interfejs MLDBM dodając obsługę jednoczesnego
dostępu do baz danych MLDBM z blokowaniem plików i zrzuca operacje
wejścia/wyjścia dla danej blokady. Nowe API Lock()/Unlock() może być
używane do logicznej serializacji żądań i zwiększenia wydajności dla
szeregu operacji odczytu i zapisu.

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
%doc CHANGES README
%{perl_vendorlib}/MLDBM/Sync.pm
%dir %{perl_vendorlib}/MLDBM/Sync
%{perl_vendorlib}/MLDBM/Sync/SDBM_File.pm
%{_mandir}/man3/*
