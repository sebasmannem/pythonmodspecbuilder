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
./configure
make

%install
make install -o $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files

%changelog
* Tue Oct 10 2017 - S. Mannem <sebas@mannem.nl>
- Initial build of this spec
