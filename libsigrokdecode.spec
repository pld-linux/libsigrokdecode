#
# Conditional build:
%bcond_without	static_libs	# stqatic library

Summary:	Basic API for running protocol decoders
Summary(pl.UTF-8):	Podstawowe API do uruchamiana dekoderów protokołów
Name:		libsigrokdecode
Version:	0.3.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://www.sigrok.org/download/source/libsigrokdecode/%{name}-%{version}.tar.gz
# Source0-md5:	c2c134355a0c50404e692335ce5b4c6e
URL:		http://www.sigrok.org/
# for unit tests
#BuildRequires:	check >= 0.9.4
BuildRequires:	doxygen
BuildRequires:	gcc >= 6:4.0
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	graphviz
# for protocol decoder tests
#BuildRequires:	libsigrok-devel >= 0.3.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
Requires:	glib2 >= 1:2.24.0
Requires:	python3-modules
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
Requires:	glib2-devel >= 1:2.24.0
Requires:	python3-devel >= 1:3.2

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
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsigrokdecode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsigrokdecode.so.2
%{_datadir}/libsigrokdecode

%files devel
%defattr(644,root,root,755)
%doc doxy/html-api/*
%attr(755,root,root) %{_libdir}/libsigrokdecode.so
%{_includedir}/libsigrokdecode
%{_pkgconfigdir}/libsigrokdecode.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsigrokdecode.a
%endif
