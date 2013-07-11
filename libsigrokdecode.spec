# TODO
# - py2/py3 bindings?
Summary:	Basic API for running protocol decoders
Name:		libsigrokdecode
Version:	0.2.0
Release:	1
License:	GPL v3+
Group:		Libraries
URL:		http://www.sigrok.org/
Source0:	http://www.sigrok.org/download/source/libsigrokdecode/%{name}-%{version}.tar.gz
# Source0-md5:	e5216eaf751510b12b5cfd846b970d64
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
%{name} is a shared library written in C which provides the basic API
for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-silent-rules

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
%{_includedir}/libsigrokdecode
%attr(755,root,root) %{_libdir}/libsigrokdecode.so
%{_pkgconfigdir}/libsigrokdecode.pc
