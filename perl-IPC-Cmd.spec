%define upstream_name    IPC-Cmd
%define upstream_version 0.46

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(Module::Load::Conditional)
Buildrequires:  perl-version
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
IPC::Cmd allows you to run commands, interactively if desired, platform
independent but have them still work.

The can_run function can tell you if a certain binary is installed and if so
where, whereas the run function can actually execute any of the commands you
give it and give you a clear return value, as well as adhere to your verbosity
settings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/IPC
%{_mandir}/*/*
