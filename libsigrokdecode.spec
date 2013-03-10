# TODO
# - py2/py3 bindings?
Summary:	Basic API for running protocol decoders
Name:		libsigrokdecode
Version:	0.1.0
Release:	1
License:	GPL v3+
Group:		Libraries
URL:		http://www.sigrok.org/
Source0:	http://downloads.sourceforge.net/sigrok/%{name}-%{version}.tar.gz
# Source0-md5:	9bc237972f6176ba9dcff057b4e85fd6
BuildRequires:	doxygen
BuildRequires:	glib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python3-devel
BuildRequires:	python3-modules
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libsigrokdecode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsigrokdecode.so.0
%{_datadir}/libsigrokdecode

%files devel
%defattr(644,root,root,755)
%doc README doxy/html/*
%{_includedir}/sigrokdecode.h
%attr(755,root,root) %{_libdir}/libsigrokdecode.so
%{_pkgconfigdir}/libsigrokdecode.pc
