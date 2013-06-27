%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{name}}

%define wrapper_doc_dir %{_root_datadir}/doc/%{name}-%{version}

%global rubyabi 1.9.1

Summary: Wrapper for %{scl_prefix} ruby.
Name: %{?scl:%scl_prefix}ruby-wrapper
Version: 0.0.1
Release: 2%{?dist}
Group: Development/Languages
License:  ASL 2.0 
URL: https://github.com/maxamillion/ruby-wrapper
# git clone -b 0.0.1 \
#   git://github.com/maxamillion/ruby-wrapper.git \
#   ruby-wrapper-0.0.1
#
# rm -fr ruby-wrapper-0.0.1/.git
#
# tar -cvzf ruby-wrapper-0.0.1.tar.gz ruby-wrapper-0.0.1
Source0: ruby-wrapper-%{version}.tar.gz
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
BuildArch: noarch

%description
Wrapper for %{scl_prefix} ruby so that other wrapper scripts can be 
written with a "shim." Examples can be found in the doc directory.


%prep
%setup -q -n ruby-wrapper-%{version}

%build

%install

# Create the %%{_root_bindir} wrapper:
%if 0%{?scl:1}

# Modify the shim/wrapper to include the correct scl
sed -i s/FIXMESCL/%{scl}/ ruby-wrapper

mkdir -p %{buildroot}%{_root_bindir}
install -m0755 ruby-wrapper %{buildroot}%{_root_bindir}/%{scl_prefix}ruby

mkdir -p %{buildroot}%{wrapper_doc_dir}
install -m0644 *.spec %{buildroot}%{wrapper_doc_dir}

install -m0644 doc/* %{buildroot}%{wrapper_doc_dir}

%else 
# Not SCL is an error, this should only build for SCL
exit 1
%endif

%files
%dir %{wrapper_doc_dir}
%{wrapper_doc_dir}/*

%{?scl:%{_root_bindir}/%{scl_prefix}ruby}


%changelog
* Wed Jun 26 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1-2
- Fix rubyabi 
* Wed Jun 26 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1-1
- First package of the ruby-wrapper
