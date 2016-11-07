Name:           zstr
Version:        1.0.0
Release:        1%{?dist}
Summary:        A C++ header-only ZLib wrapper

License:        MIT
URL:            https://github.com/mateidavid/zstr
Source0:        https://github.com/mateidavid/zstr/archive/v1.0.0.tar.gz
BuildArch:      noarch

%description
This C++ header-only library enables the use of C++ standard iostreams to
access ZLib-compressed streams.


%package        devel
Summary:        Development files for %{name}
Requires:       pkgconfig(zlib)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
install -p -m644 -D src/strict_fstream.hpp %{buildroot}%{_includedir}/zstr/strict_fstream.hpp
install -p -m644 -D src/zstr.hpp %{buildroot}%{_includedir}/zstr/zstr.hpp


%files devel
%license LICENSE
%doc README.org examples
%{_includedir}/*


%changelog
* Mon Nov 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1
- Public release
