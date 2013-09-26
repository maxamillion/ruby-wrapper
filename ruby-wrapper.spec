%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{name}}

%define wrapper_doc_dir %{_root_datadir}/doc/%{name}-%{version}

%global rubyabi 1.9.1

Summary: Wrapper for %{scl_prefix} ruby.
Name: %{?scl:%scl_prefix}ruby-wrapper
Version: 0.0.2
Release: 3%{?dist}
Group: Development/Languages
License:  ASL 2.0
URL: https://github.com/maxamillion/ruby-wrapper
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Source0: ruby-wrapper
Source1: ruby-wrapper-rake
Source2: ruby-wrapper-rails
Source3: LICENSE
Source4: README
Source5: example_shim
BuildArch: noarch

%description
Wrapper for %{scl_prefix} ruby so that other wrapper scripts can be
written with a "shim." Examples can be found in the doc directory.

%install

# Create the %%{_root_bindir} wrapper:
%if 0%{?scl:1}
mkdir -p %{buildroot}%{_root_bindir}
install -p -m0755 %{SOURCE0} %{buildroot}%{_root_bindir}/%{scl_prefix}ruby
install -p -m0755 %{SOURCE1} %{buildroot}%{_root_bindir}/%{scl_prefix}rake
install -p -m0755 %{SOURCE2} %{buildroot}%{_root_bindir}/%{scl_prefix}rails

# Modify the shim/wrapper to include the correct scl
sed -i s/FIXMESCL/%{scl}/ %{buildroot}%{_root_bindir}/%{scl_prefix}ruby
sed -i s/FIXMESCL/%{scl}/ %{buildroot}%{_root_bindir}/%{scl_prefix}rake
sed -i s/FIXMESCL/%{scl}/ %{buildroot}%{_root_bindir}/%{scl_prefix}rails

mkdir -p %{buildroot}%{wrapper_doc_dir}

install -p -m0644 %{SOURCE3} %{buildroot}%{wrapper_doc_dir}/LICENSE
install -p -m0644 %{SOURCE4} %{buildroot}%{wrapper_doc_dir}/README
install -p -m0644 %{SOURCE5} %{buildroot}%{wrapper_doc_dir}/example_shim

%else 
# Not SCL is an error, this should only build for SCL
exit 1
%endif

%files
%dir %{wrapper_doc_dir}
%{wrapper_doc_dir}/*

%{?scl:%{_root_bindir}/%{scl_prefix}ruby}
%{?scl:%{_root_bindir}/%{scl_prefix}rake}


%changelog
* Wed Sep 18 2013 Sam Kottler <shk@redhat.com> -0.0.2-3
* Add a rails wrapper
* Mon Sep 9 2013 Sam Kottler <shk@redhat.com> - 0.0.2-2
- Move /usr/bin/ruby193-ruby-rake to /usr/bin/ruby193-rake
* Mon Sep 9 2013 Sam Kottler <shk@redhat.com> - 0.0.2-1
- Add prefixed rake wrapper
* Wed Jun 26 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1-2
- Fix rubyabi 
* Wed Jun 26 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1-1
- First package of the ruby-wrapper
