%define upstream_name    IPC-Cmd
%define upstream_version 0.92
Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        1

Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/IPC/IPC-Cmd-%{upstream_version}.tar.gz

Buildrequires:  perl-devel
Buildrequires:  perl(Module::Load::Conditional)
Buildrequires:  perl(version)

Buildarch:      noarch

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
%make test

%install
%makeinstall_std

%clean 

%files 
%doc README
%{perl_vendorlib}/IPC
%{_mandir}/*/*


%changelog
* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.640.0-2mdv2012.0
+ Revision: 764839
- rebuild

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 597098
- update to 0.64

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-3mdv2011.0
+ Revision: 562426
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-2mdv2011.0
+ Revision: 558162
- rebuild

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2011.0
+ Revision: 551222
- update to 0.60

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.560.0-1mdv2010.1
+ Revision: 501137
- update to 0.56

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.540.0-1mdv2010.1
+ Revision: 468934
- update to 0.54

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 437213
- update to 0.50

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.0
+ Revision: 402561
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.46-1mdv2010.0
+ Revision: 387008
- update to new version 0.46

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2010.0
+ Revision: 372109
- update to new version 0.44

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2009.1
+ Revision: 292191
- update to new version 0.42

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.40-3mdv2009.0
+ Revision: 257369
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2008.1
+ Revision: 104498
- update to new version 0.40

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2008.1
+ Revision: 97658
- update to new version 0.38


* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2007.0
+ Revision: 87852
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2007.1
+ Revision: 86576
- new revision

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2007.1
+ Revision: 84468
- Import perl-IPC-Cmd

* Sat Sep 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2007.0
- new version
- fix sources URL

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-2mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdk
- first mdk release






