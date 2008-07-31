%define module  IPC-Cmd
%define name    perl-%{module}
%define version 0.40
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Finding and running system commands made easy
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/IPC/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(Module::Load::Conditional)
Buildrequires:  perl-version
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
IPC::Cmd allows you to run commands, interactively if desired, platform
independent but have them still work.

The can_run function can tell you if a certain binary is installed and if so
where, whereas the run function can actually execute any of the commands you
give it and give you a clear return value, as well as adhere to your verbosity
settings.

%prep
%setup -q -n %{module}-%{version}

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


