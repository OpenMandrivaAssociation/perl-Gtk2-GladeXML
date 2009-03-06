%define module Gtk2-GladeXML
%define fmodule Glade

Summary: Perl module for the glade libraries
Name:    perl-%module
Version: 1.007
Release: %mkrel 2
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


