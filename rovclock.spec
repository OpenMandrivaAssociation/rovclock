Name:           rovclock
Version:        0.6e
Release:        6
Epoch:          0
Summary:        Radeon overclocking utility
License:        GPL
Group:          System/Kernel and hardware
URL:            https://www.hasw.net/linux/
Source0:        http://www.hasw.net/linux/rovclock-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rovclock is a Radeon overclocking utility.

The cards that are reported to work are:

Radeon 7500
Radeon 8500
Radeon 9000
Radeon 9100
Radeon 9500 (Pro)
Radeon 9550
Radeon 9600
Mobility FireGL T2
Mobility Radeon 9600 M10
Radeon 9700 (Pro)
Radeon X550
Radeon X800XL

%prep
%setup -q

%build
%{make} CC=%{__cc} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a %{name} %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root,0755)
%doc ChangeLog COPYING README 
%attr(0755,root,root) %{_bindir}/%{name}




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:0.6e-5mdv2010.0
+ Revision: 433354
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:0.6e-4mdv2009.0
+ Revision: 260280
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:0.6e-3mdv2009.0
+ Revision: 251370
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:0.6e-1mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 David Walluck <walluck@mandriva.org> 0.6e-1mdv2007.0
+ Revision: 103585
- Import rovclock

* Tue Dec 05 2006 David Walluck <walluck@mandriva.org> 0:0.6e-1mdv2007.1
- release

