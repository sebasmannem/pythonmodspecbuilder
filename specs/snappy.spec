Summary: 	Snappy, a fast compressor/decompressor.
Name: 		snappy
Version: 	1.1.3
Release: 	1%{?dist}
License: 	BSD
Group: 		Development/Libraries
Url: 		https://github.com/google/snappy
Source0:        %{name}-%{version}.tar.gz
BuildArch: 	x86_64

%description
Snappy is a compression/decompression library. It does not aim for maximum compression, or compatibility with any other compression library; instead, it aims for very high speeds and reasonable compression. For instance, compared to the fastest mode of zlib, Snappy is an order of magnitude faster for most inputs, but the resulting compressed files are anywhere from 20% to 100% bigger. 

%prep
%setup -n %{name}-%{version} -q

%build
%configure
%make_build

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libsnappy.so*
%{_docdir}/snappy
%exclude %{_libdir}/libsnappy.a
%exclude %{_libdir}/libsnappy.la

%package devel
summary: Development libraries for snappy, a fast compressor/decompressor.

%description devel
Snappy is a compression/decompression library. It does not aim for maximum compression, or compatibility with any other compression library; instead, it aims for very high speeds and reasonable compression. For instance, compared to the fastest mode of zlib, Snappy is an order of magnitude faster for most inputs, but the resulting compressed files are anywhere from 20% to 100% bigger.

%files devel
%{_prefix}/include*


%changelog
* Tue Oct 10 2017 - S. Mannem <smannem@bol.com>
- Initial build of this spec
