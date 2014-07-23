# TODO
# - py2/py3 bindings?
#
# Conditional build:
%bcond_without	static_libs	# stqatic library

Summary:	Basic API for running protocol decoders
Summary(pl.UTF-8):	Podstawowe API do uruchamiana dekoderów protokołów
Name:		libsigrokdecode
Version:	0.2.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://www.sigrok.org/download/source/libsigrokdecode/%{name}-%{version}.tar.gz
# Source0-md5:	e5216eaf751510b12b5cfd846b970d64
URL:		http://www.sigrok.org/
BuildRequires:	doxygen
BuildRequires:	glib2-devel
BuildRequires:	graphviz
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsigrokdecode is a shared library written in C which provides the
basic API for running sigrok protocol decoders. The protocol decoders
themselves are written in Python.

%description -l pl.UTF-8
libsigrokdecode to napisana w C biblioteka współdzielona
udostępniająca podstawowe API do uruchamiania dekoderów protokołów
sigrok. Same dekodery protokołów są napisane w Pythonie.

%package devel
Summary:	Development files for libsigrokdecode
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libsigrokdecode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libsigrokdecode.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libsigrokdecode.

%package static
Summary:	Static libsigrokdecode library
Summary(pl.UTF-8):	Statyczna biblioteka libsigrokdecode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsigrokdecode library.

%description static -l pl.UTF-8
Statyczna biblioteka libsigrokdecode.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

# This builds documentation for the -doc package
doxygen Doxyfile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsigrokdecode.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libsigrokdecode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsigrokdecode.so.1
%{_datadir}/libsigrokdecode

%files devel
%defattr(644,root,root,755)
%doc README doxy/html-api/*
%attr(755,root,root) %{_libdir}/libsigrokdecode.so
%{_includedir}/libsigrokdecode
%{_pkgconfigdir}/libsigrokdecode.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsigrokdecode.a
%endif
