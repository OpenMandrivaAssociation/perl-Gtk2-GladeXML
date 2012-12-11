%define module Gtk2-GladeXML
%define fmodule Glade

Summary: Perl module for the glade libraries
Name:    perl-%module
Version: 1.007
Release:	4
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: libglade2.0-devel perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2
BuildRequires: glitz-devel
Requires: perl-Gtk2 
Conflicts: drakxtools < 9.1-15mdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds perl support for Glade 2.x to Gtk2-Perl.

libglade allows to load externally stored user interfaces in programs
This allows alteration of GUIes without recompiling of programs.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*




%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.007-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.007-3mdv2011.0
+ Revision: 440569
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.007-2mdv2009.1
+ Revision: 350224
- 2009.1 rebuild

* Mon Sep 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.007-1mdv2009.0
+ Revision: 282568
- update to new version 1.007

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.006-5mdv2009.0
+ Revision: 257165
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.006-3mdv2008.1
+ Revision: 152104
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 1.006-2mdv2008.0
+ Revision: 44603
- rebuild


* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.006-1mdv2007.0
+ Revision: 86939
- Import perl-Gtk2-GladeXML

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.006-1mdv2007.1
- new release

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.005-1mdk
- new release

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.001-3mdk
- buildrequires fix

* Thu Dec 02 2004 Austin Acton <austin@mandrake.org> 1.001-2mdk
- rebuild without multithread

* Fri Sep 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.001-1mdk
- new release

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-4mdk
- rebuild for perl-5.8.5

* Tue Apr 06 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-3mdk
- package examples

* Sat Apr 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-2mdk
- remove references to never uploaded releases

* Fri Apr 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-1mdk
- new release
- fix buildrequires
- really use versionned tarball :-(
- kill useless patch 0

* Tue Feb 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.95-2mdk
- rebuild (thus s/5.8.2/5.8.3/ in installation directory thus fixing DIRM)

* Mon Jan 12 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.95-1mdk
- new release

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.93-1mdk
- new release
- rename spec file
- patch 0: fix build

