%global scl_version ea-php70
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcache
Version: 3.0.8
Summary: memcache extension for %{scl_version}
Release: 1%{?dist}
License: MIT
Group: Programming/Languages
URL: https://github.com/websupport-sk/pecl-memcache/
Source: https://github.com/websupport-sk/pecl-memcache/archive/NON_BLOCKING_IO_php7.tar.gz?/pecl-memcache-NON_BLOCKING_IO_php7.tar.gz
Source1: memcache.ini

# should be no requires for building this package
#Requires: memcached
#BuildRequires: libyaml-devel
BuildRequires: %{scl_version} %{scl_version}-php-cli

%description
Memcached is a caching daemon designed especially for  dynamic web applications
to decrease database load by storing objects in memory. This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -n pecl-memcache-NON_BLOCKING_IO_php7

%build
scl enable %{scl_version} phpize
scl enable %{scl_version} ./configure
make

%install
#scl enable %{scl_version} 'make install DESTDIR=$RPM_BUILD_ROOT'
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcache.so
%config /%{ext_prefix}/%{conf_dir}/memcache.ini

%changelog
* Mon Mar  6 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- added ea-php71-php-memcahe branched off of php54

* Fri Mar  5 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- Fixed package name, entire RPM is now working.

* Wed Mar  1 2017 Jack Hayhurst <jack@deleteos.com> - 0.1
- Initial spec file creation.
